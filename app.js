function checkPerfume() {
    var name = document.getElementById('perfumeName').value;
    fetch('/perfume?name=' + name)
        .then(response => response.json())
        .then(data => document.getElementById('result').textContent = data.message);
}

function getPerfumes() {
    fetch('/perfumes')
        .then(response => response.json())
        .then(data => document.getElementById('result').textContent = data.perfumes.join(', '));
}