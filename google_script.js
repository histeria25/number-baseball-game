/* [사용 방법] 
   1. 구글 스프레드시트 생성 -> 확장 프로그램 -> Apps Script 클릭
   2. 아래 코드를 복사해서 붙여넣고 저장
   3. '배포' -> '새 배포' -> 유형: 웹 앱 -> 액세스 권한: 모든 사용자 설정 후 배포
   4. 생성된 웹 앱 URL을 script.js의 fetch 부분에 넣기
*/

function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = JSON.parse(e.postData.contents);
  
  // 데이터 추가: [날짜, 이름, 시도 횟수]
  sheet.appendRow([new Date().toLocaleString(), data.name, data.tries]);
  
  return ContentService.createTextOutput(JSON.stringify({"result": "success"}))
    .setMimeType(ContentService.MimeType.JSON);
}

// CORS 에러 방지를 위한 doGet 설정
function doGet(e) {
  return ContentService.createTextOutput("GAS 서버가 작동 중입니다.");
}