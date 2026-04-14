const { checkAnswer } = require('./script.js');
const result = checkAnswer(123, 134);
if (result.strike === 1 && result.ball === 1) {
  process.exit(0); // 성공
} else {
  process.exit(1); // 실패
}
