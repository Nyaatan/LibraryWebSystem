var pdfjsLib = window['pdfjs-dist/build/pdf'];
const workerUrl = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.5.207/build/pdf.worker.min.js';
pdfjsLib.GlobalWorkerOptions.workerSrc = workerUrl;

var bookObject = null;
var pageNum = 1;
var pageRendering = false;
var pageNumPending = null;
var pageScale = 1.0;
var bookCanvas = null;
var bookContext = null;
var bookContainer = null;
var bookCanvasWidth = 0;

const BOTTOM_SPACE = 50;

window.onload = function() {
    bookCanvas = document.getElementById('bookPageView');
    bookContext = bookCanvas.getContext('2d');
    bookContainer = document.getElementById('bookPageContainer');
    bookCanvasWidth = getAvailableWidth(bookContainer);
    pdfjsLib.getDocument(streamBaseUrl + '?isbn=' + bookIsbn).promise.then(function(pdfObject) {
        bookObject = pdfObject;
        document.getElementById('pageCount').textContent = bookObject.numPages;
        renderPage(pageNum);
    }, function (reason) {
        console.error(reason);
    });
    window.onresize = function() {
        bookCanvasWidth = getAvailableWidth(bookContainer);
        queueRenderPage(pageNum);
    };
    document.getElementById('prevPage').onclick = goToPrevPage;
    document.getElementById('nextPage').onclick = goToNextPage;
    document.getElementById('zoomIn').onclick = zoomInPage;
    document.getElementById('zoomOut').onclick = zoomOutPage;
}

function renderPage(num) {
    pageRendering = true;
    bookObject.getPage(num).then(function(page) {
        var originalWidth = page.getViewport({scale: 1}).width;
        var bookViewport = page.getViewport({scale: (bookCanvasWidth * pageScale / originalWidth)});
        console.log("bookCanvas.width: " + bookCanvas.width);
        console.log("bookCanvas.height: " + bookCanvas.height );
        bookCanvas.width = bookViewport.width;
        bookCanvas.height = bookViewport.height;
        bookCanvas.style.width  = bookViewport.width + 'px';
        bookCanvas.style.height = bookViewport.height + 'px';
        console.log("bookCanvas.width1:" + bookCanvas.width);
        console.log("bookCanvas.height1: " + bookCanvas.height );

        var renderContext = {
            canvasContext: bookContext,
            viewport: bookViewport
        };
        var renderTask = page.render(renderContext);

        renderTask.promise.then(function() {
            pageRendering = false;
            if (pageNumPending !== null) {
                renderPage(pageNumPending);
                pageNumPending = null;
            }
            bookContainer.style.height = 
                (window.innerHeight - bookContainer.getBoundingClientRect().top 
                - BOTTOM_SPACE) + "px";
        });
    });
    document.getElementById('pageNumber').textContent = num;
}

function goToPrevPage() {
    if (pageNum <= 1) {
        return;
    }
    --pageNum;
    queueRenderPage(pageNum);
}

function goToNextPage() {
    if (pageNum >= bookObject.numPages) {
        return;
    }
    ++pageNum;
    queueRenderPage(pageNum);
}

function zoomInPage() {
    pageScale += 0.2;
    queueRenderPage(pageNum);
}

function zoomOutPage() {
    pageScale -= 0.2;
    queueRenderPage(pageNum);
}

function queueRenderPage(num) {
    if (pageRendering) {
        pageNumPending = num;
    } else {
        renderPage(num);
    }
}

function getAvailableWidth(element) {
    return element.getBoundingClientRect().width 
        - element.offsetWidth + element.clientWidth;
}