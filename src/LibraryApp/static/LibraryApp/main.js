document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('loading-spinner').hidden = true;
});

function previousPage(i){
    if(i>1) {
        let x = 'p=' + (i - 1);
        location.href = location.href.replace(/p=\d*/, x)
    } else location.reload();
}

function nextPage(i){
    let x = 'p=' + (i + 1);
    location.href = location.href.replace(/p=\d*/, x)
}

