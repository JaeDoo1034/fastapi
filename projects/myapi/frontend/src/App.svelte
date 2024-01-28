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
{/await}
