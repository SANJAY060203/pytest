from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """
<!doctype html>
<title>FastAPI Echo Page</title>
<form id="f">
  <input id="text" name="text" />
  <button id="btn" type="submit">Send</button>
</form>
<div id="result"></div>
<script>
document.getElementById('f').addEventListener('submit', function(e){
  e.preventDefault();
  const t = document.getElementById('text').value;
  document.getElementById('result').textContent = 'Echo: ' + t;
});
</script>
"""

@app.get("/", response_class=HTMLResponse)
def index():
    return HTML
