(function() {
    var vizPrefix = "language-viz-";
    Array.prototype.forEach.call(document.querySelectorAll("[class^=" + vizPrefix + "]"), function(x) {
        var engine;
        x.getAttribute("class").split(" ").forEach(function(cls) {
            if (cls.startsWith(vizPrefix)) {
                engine = cls.substr(vizPrefix.length);
            }
        });
        var image = new DOMParser().parseFromString(Viz(x.innerText, { format: "svg", engine: engine }), "image/svg+xml");
        x.parentNode.insertBefore(image.documentElement, x);
        x.style.display = 'none'
    });
})();