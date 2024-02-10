<!-- message 띄우는 예시 -->
<!-- <script> 동기 방식
  let message;

  fetch("http://127.0.0.1:8000/hello").then((response) => {
    response.json().then((json) => {
      message = json.message;
    });
  });
</script> -->

<!-- 비동기 방식  : chatgpt-->
<!-- <script>
  let message;

  async function fetchMessage() {
    const response = await fetch("http://127.0.0.1:8000/hello");
    const json = await response.json();
    message = json.message;
  }

  fetchMessage();
</script> -->
<!-- 
<script>
  async function hello() {
    const res = await fetch("http://127.0.0.1:8000/hello");
    const json = await res.json();

    if (res.ok) {
      return json.message;
    } else {
      alert("error");
    }
  }

  let promise = hello();
</script>

{#await promise}
  <p>...waiting</p>
{:then message}
  <h1>{message}</h1>
{/await} -->

<script>
  let question_list = [];
  // 위처럼 초깃값을 주지 않을 경우, fetch함수는 비동기 방식으로 실행되기 때문에, 요청하는 HTML 영역의 each 문이 실행되고 question_list에 값이 없어 오류 발생.
  // 따라서 반복문과 함께 사용할 경우 해당 값을 빈 리스트로 초기화 하는 것이 좋다.
  // 혹은 해당 값이 있는 지를 체크하는 로직을 each 문 앞에 사용.

  function get_question_list() {
    fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
      response.json().then((json) => {
        question_list = json;
      });
    });
  }
  get_question_list();
</script>

<ul>
  <!--each 문에서 index 생략 가능.-->
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>
