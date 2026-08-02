from pathlib import Path


# 현재 폴더에서 PyExam_Pro HTML 원본을 찾습니다.
current_folder = Path(__file__).resolve().parent

html_files = [
    file
    for file in current_folder.glob("PyExam_Pro*.html")
    if file.name != "PyExam_Pro_수정완료.html"
]

if not html_files:
    raise FileNotFoundError(
        "같은 폴더에서 PyExam_Pro로 시작하는 HTML 파일을 찾지 못했습니다."
    )

# 같은 이름의 파일이 여러 개라면 가장 최근 파일을 선택합니다.
source_file = max(html_files, key=lambda file: file.stat().st_mtime)
output_file = current_folder / "PyExam_Pro_수정완료.html"

html = source_file.read_text(encoding="utf-8")


def replace_between(text, start_marker, end_marker, replacement):
    start_index = text.find(start_marker)

    if start_index == -1:
        raise ValueError(f"시작 코드를 찾지 못했습니다:\n{start_marker}")

    end_index = text.find(end_marker, start_index)

    if end_index == -1:
        raise ValueError(f"종료 코드를 찾지 못했습니다:\n{end_marker}")

    return text[:start_index] + replacement + text[end_index:]


# 1. 잘못된 DOCTYPE 수정
html = html.replace("<!DOCTYPE 1 html>", "<!DOCTYPE html>", 1)


# 2. 모의고사에서 선택한 답안을 표시하는 CSS 추가
mock_css = """
      /* 모의고사에서 현재 선택한 객관식 답안 */
      .option-btn.mock-selected {
        border-color: var(--primary);
        background: rgba(79, 70, 229, 0.15);
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.12);
        font-weight: 700;
      }

      .option-btn:disabled {
        cursor: default;
        opacity: 1;
      }

"""

css_marker = "      /* Detailed View Modal / Expansion */"

if ".option-btn.mock-selected" not in html:
    html = html.replace(css_marker, mock_css + css_marker, 1)


# 3. localStorage 오류 때문에 전체 버튼이 멈추는 문제 방지
state_start = "      let state = {"
state_end = """      /* ==========================================================================
           NAVIGATION & THEME"""

new_state_code = r"""      // 저장 데이터가 손상되었거나 브라우저가 localStorage를 차단해도
      // 웹앱 전체가 중단되지 않도록 안전하게 처리합니다.
      function safeGetItem(key, fallback = null) {
        try {
          const value = localStorage.getItem(key);
          return value === null ? fallback : value;
        } catch (error) {
          console.warn(`localStorage 읽기 실패: ${key}`, error);
          return fallback;
        }
      }

      function safeGetJSON(key, fallback) {
        try {
          const value = safeGetItem(key, null);
          return value === null ? fallback : JSON.parse(value);
        } catch (error) {
          console.warn(`저장 데이터 복구: ${key}`, error);
          return fallback;
        }
      }

      function safeSetItem(key, value) {
        try {
          localStorage.setItem(key, value);
        } catch (error) {
          console.warn(`localStorage 저장 실패: ${key}`, error);
        }
      }

      function safeRemoveItem(key) {
        try {
          localStorage.removeItem(key);
        } catch (error) {
          console.warn(`localStorage 삭제 실패: ${key}`, error);
        }
      }

      let state = {
        completedConcepts: safeGetJSON('py_completed_concepts', []),
        quizAnswers: safeGetJSON('py_quiz_answers', {}),
        bookmarks: safeGetJSON('py_bookmarks', []),
        wrongAnswers: safeGetJSON('py_wrong_answers', []),
        theme: safeGetItem('py_theme', 'light'),
      };

      function saveState() {
        safeSetItem(
          'py_completed_concepts',
          JSON.stringify(state.completedConcepts),
        );
        safeSetItem(
          'py_quiz_answers',
          JSON.stringify(state.quizAnswers),
        );
        safeSetItem(
          'py_bookmarks',
          JSON.stringify(state.bookmarks),
        );
        safeSetItem(
          'py_wrong_answers',
          JSON.stringify(state.wrongAnswers),
        );
        safeSetItem('py_theme', state.theme);

        updateDashboardStats();
      }

"""

html = replace_between(html, state_start, state_end, new_state_code)


# 4. 일반 문제와 모의고사 문제를 각각 정상적으로 렌더링하도록 수정
quiz_render_start = "      function renderSingleQuizCard(q, isMock = false) {"
quiz_render_end = """      /* ==========================================================================
           QUIZ INTERACTION LOGIC"""

new_quiz_render = r"""      function renderSingleQuizCard(q, isMock = false) {
        // 모의고사에서는 기존 연습 문제 풀이 기록을 사용하지 않습니다.
        const userAns = isMock ? undefined : state.quizAnswers[q.id];
        const isBookmarked = state.bookmarks.includes(q.id);

        let optionsHtml = '';

        if (q.type === 'MC') {
          optionsHtml =
            `<div class="options-grid">` +
            q.opts
              .map((opt, idx) => {
                let btnClass = 'option-btn';

                if (!isMock && userAns !== undefined) {
                  if (idx === q.ans) {
                    btnClass += ' correct';
                  } else if (
                    userAns.userAns === idx &&
                    !userAns.isCorrect
                  ) {
                    btnClass += ' wrong';
                  }
                }

                let clickCode = '';

                if (isMock) {
                  clickCode =
                    `onclick="selectMockMC('${q.id}', ${idx}, this)"`;
                } else if (userAns === undefined) {
                  clickCode =
                    `onclick="submitMC('${q.id}', ${idx})"`;
                }

                return `
                  <button
                    type="button"
                    class="${btnClass}"
                    ${clickCode}
                  >
                    ${idx + 1}. ${escapeHtml(opt)}
                  </button>
                `;
              })
              .join('') +
            `</div>`;
        } else {
          const isAnswered = userAns !== undefined;
          const previousInput = isAnswered
            ? String(userAns.userAns)
            : '';

          optionsHtml = `
            <div class="short-answer-group">
              <input
                type="text"
                class="short-answer-input"
                id="sa-input-${q.id}"
                value="${escapeHtml(previousInput)}"
                placeholder="정답을 입력하세요..."
                ${isAnswered ? 'disabled' : ''}
              >

              ${
                !isAnswered && !isMock
                  ? `
                    <button
                      type="button"
                      class="submit-sa-btn"
                      onclick="submitSA('${q.id}')"
                    >
                      정답 확인
                    </button>
                  `
                  : ''
              }
            </div>
          `;
        }

        const showExplanation =
          userAns !== undefined && !isMock;

        const retryButton =
          userAns !== undefined && !isMock
            ? `
              <button
                type="button"
                class="submit-sa-btn"
                style="
                  width: 100%;
                  margin-top: 10px;
                  background: var(--text-muted);
                "
                onclick="resetQuizAnswer('${q.id}')"
              >
                🔄 다시 풀기
              </button>
            `
            : '';

        const answerText =
          q.type === 'MC'
            ? `${q.ans + 1}번 (${escapeHtml(q.opts[q.ans])})`
            : q.ans.map((answer) => escapeHtml(answer)).join(' 또는 ');

        return `
          <div
            class="quiz-card"
            id="quiz-card-${q.id}"
            data-quiz-id="${q.id}"
          >
            <div class="quiz-header">
              <div class="badge-group">
                <span class="badge badge-unit">${q.unit}</span>
                <span class="badge badge-freq-mid">
                  난이도: ${q.diff}
                </span>
                <span class="badge badge-unit">
                  ${q.type === 'MC' ? '객관식' : '단답형'}
                </span>
              </div>

              <button
                type="button"
                class="bookmark-btn ${
                  isBookmarked ? 'active' : ''
                }"
                onclick="toggleBookmark('${q.id}')"
              >
                <i class="fa-solid fa-star"></i>
              </button>
            </div>

            <div class="quiz-question">${escapeHtml(q.q)}</div>

            ${optionsHtml}

            <div
              class="quiz-explanation ${
                showExplanation ? 'show' : ''
              }"
              id="exp-${q.id}"
            >
              <div
                class="quiz-result-message"
                style="
                  font-weight: 700;
                  color: ${
                    userAns && userAns.isCorrect
                      ? 'var(--accent)'
                      : 'var(--accent-danger)'
                  };
                  margin-bottom: 0.5rem;
                "
              >
                ${
                  userAns
                    ? userAns.isCorrect
                      ? '⭕ 정답입니다!'
                      : '❌ 오답입니다!'
                    : ''
                }
              </div>

              <p>
                <strong>정답:</strong>
                ${answerText}
              </p>

              <p style="margin-top: 4px">
                <strong>해설:</strong>
                ${escapeHtml(q.exp)}
              </p>

              <p
                style="
                  margin-top: 4px;
                  color: var(--primary);
                "
              >
                <strong>시험 포인트:</strong>
                ${escapeHtml(q.point)}
              </p>
            </div>

            ${retryButton}
          </div>
        `;
      }

"""

html = replace_between(
    html,
    quiz_render_start,
    quiz_render_end,
    new_quiz_render,
)


# 5. 모의고사 선택, 채점, 재시작 기능 전체 수정
mock_start = "      let mockQuestions = [];"
mock_end = """      /* ==========================================================================
           WRONG ANSWERS & BOOKMARKS"""

new_mock_code = r"""      let mockQuestions = [];
      let mockAnswers = {};
      let examTimerInterval = null;
      let mockSubmitted = false;

      function selectMockMC(qId, selectedIndex, selectedButton) {
        if (mockSubmitted) return;

        mockAnswers[qId] = selectedIndex;

        const card = document.getElementById(`quiz-card-${qId}`);
        if (!card) return;

        card.querySelectorAll('.option-btn').forEach((button) => {
          button.classList.remove('mock-selected');
        });

        selectedButton.classList.add('mock-selected');
      }

      function startMockExam() {
        const countElement = document.getElementById('mockCount');
        const count = Number.parseInt(countElement.value, 10);

        mockQuestions = [...QUIZ_DATA]
          .sort(() => Math.random() - 0.5)
          .slice(0, count);

        mockAnswers = {};
        mockSubmitted = false;

        const container =
          document.getElementById('mockQuizContainer');

        container.innerHTML = mockQuestions
          .map((q) => renderSingleQuizCard(q, true))
          .join('');

        document.getElementById('mockSetup').style.display = 'none';
        document.getElementById('btnSubmitMock').style.display = 'block';
        document.getElementById('mockResult').style.display = 'none';
        document.getElementById('examTimer').innerText = '60:00';

        let timeLeft = 60 * 60;

        clearInterval(examTimerInterval);

        examTimerInterval = setInterval(() => {
          timeLeft -= 1;

          const minutes = Math.floor(timeLeft / 60);
          const seconds = timeLeft % 60;

          document.getElementById('examTimer').innerText =
            `${String(minutes).padStart(2, '0')}:` +
            `${String(seconds).padStart(2, '0')}`;

          if (timeLeft <= 0) {
            clearInterval(examTimerInterval);
            submitMockExam();
          }
        }, 1000);

        window.scrollTo({
          top: 0,
          behavior: 'smooth',
        });
      }

      function submitMockExam() {
        if (mockSubmitted || mockQuestions.length === 0) {
          return;
        }

        mockSubmitted = true;
        clearInterval(examTimerInterval);

        let score = 0;
        let answeredCount = 0;

        mockQuestions.forEach((q) => {
          const card =
            document.getElementById(`quiz-card-${q.id}`);

          if (!card) return;

          let isCorrect = false;
          let hasAnswer = false;

          if (q.type === 'MC') {
            const selectedIndex = mockAnswers[q.id];
            const buttons = card.querySelectorAll('.option-btn');

            hasAnswer = selectedIndex !== undefined;
            isCorrect =
              hasAnswer && selectedIndex === q.ans;

            buttons.forEach((button, index) => {
              button.disabled = true;
              button.removeAttribute('onclick');
              button.classList.remove('mock-selected');

              if (index === q.ans) {
                button.classList.add('correct');
              }

              if (
                hasAnswer &&
                index === selectedIndex &&
                selectedIndex !== q.ans
              ) {
                button.classList.add('wrong');
              }
            });
          } else {
            const input =
              card.querySelector('.short-answer-input');

            if (input) {
              const userValue =
                input.value.trim().toLowerCase();

              hasAnswer = userValue.length > 0;

              isCorrect =
                hasAnswer &&
                q.ans.some(
                  (answer) =>
                    answer.toLowerCase().trim() === userValue,
                );

              input.disabled = true;

              input.style.borderColor = isCorrect
                ? 'var(--accent)'
                : 'var(--accent-danger)';

              input.style.background = isCorrect
                ? 'rgba(34, 197, 94, 0.12)'
                : 'rgba(239, 68, 68, 0.12)';
            }
          }

          if (hasAnswer) {
            answeredCount += 1;
          }

          if (isCorrect) {
            score += 1;
          } else if (!state.wrongAnswers.includes(q.id)) {
            state.wrongAnswers.push(q.id);
          }

          const explanation =
            card.querySelector('.quiz-explanation');

          if (explanation) {
            explanation.classList.add('show');

            const resultMessage =
              explanation.querySelector('.quiz-result-message');

            if (resultMessage) {
              if (!hasAnswer) {
                resultMessage.textContent =
                  '⚠️ 답을 입력하지 않은 문제입니다.';
                resultMessage.style.color =
                  'var(--accent-warning)';
              } else if (isCorrect) {
                resultMessage.textContent =
                  '⭕ 정답입니다!';
                resultMessage.style.color =
                  'var(--accent)';
              } else {
                resultMessage.textContent =
                  '❌ 오답입니다!';
                resultMessage.style.color =
                  'var(--accent-danger)';
              }
            }
          }
        });

        saveState();

        const resultDiv =
          document.getElementById('mockResult');

        const percent = Math.round(
          (score / mockQuestions.length) * 100,
        );

        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
          <h3
            style="
              color: var(--primary);
              margin-bottom: 0.5rem;
            "
          >
            🎉 채점 결과:
            ${score} / ${mockQuestions.length}문제 정답
            (${percent}점)
          </h3>

          <p>
            응답한 문제: ${answeredCount} /
            ${mockQuestions.length}
          </p>

          <p style="margin-top: 6px">
            틀리거나 답하지 않은 문제는 오답노트에 저장되었습니다.
          </p>

          <button
            type="button"
            class="submit-sa-btn"
            style="
              margin-top: 1rem;
              width: 100%;
            "
            onclick="resetMockExam()"
          >
            🔄 새로운 모의고사 풀기
          </button>
        `;

        document.getElementById(
          'btnSubmitMock',
        ).style.display = 'none';

        resultDiv.scrollIntoView({
          behavior: 'smooth',
          block: 'center',
        });
      }

      function resetMockExam() {
        clearInterval(examTimerInterval);

        mockQuestions = [];
        mockAnswers = {};
        mockSubmitted = false;

        document.getElementById(
          'mockQuizContainer',
        ).innerHTML = '';

        document.getElementById(
          'mockSetup',
        ).style.display = 'flex';

        document.getElementById(
          'btnSubmitMock',
        ).style.display = 'none';

        document.getElementById(
          'mockResult',
        ).style.display = 'none';

        document.getElementById(
          'examTimer',
        ).innerText = '60:00';

        window.scrollTo({
          top: 0,
          behavior: 'smooth',
        });
      }

"""

html = replace_between(
    html,
    mock_start,
    mock_end,
    new_mock_code,
)


# 6. 초기화 함수도 안전한 localStorage 함수로 변경
html = html.replace(
    "localStorage.removeItem('py_completed_concepts');",
    "safeRemoveItem('py_completed_concepts');",
)

html = html.replace(
    "localStorage.removeItem('py_quiz_answers');",
    "safeRemoveItem('py_quiz_answers');",
)

html = html.replace(
    "localStorage.removeItem('py_bookmarks');",
    "safeRemoveItem('py_bookmarks');",
)

html = html.replace(
    "localStorage.removeItem('py_wrong_answers');",
    "safeRemoveItem('py_wrong_answers');",
)


# 수정된 파일 저장
output_file.write_text(html, encoding="utf-8")

print("수정이 완료되었습니다.")
print(f"원본 파일: {source_file.name}")
print(f"수정 파일: {output_file.name}")
print("수정 파일을 Chrome 또는 Edge에서 열어주세요.")
