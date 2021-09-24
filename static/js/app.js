"use strict";



(function() {
    
    // loader

    document.onreadystatechange = function() {
        const container = document.querySelector('.container');
        const loader = document.querySelector('.loader');

        console.log(loader);

        if (document.readyState !== "complete") {
            container.style.display = "none";
            loader.style.display = "flex";
        } else {
            console.log('done');
            container.style.display = "block";
            loader.style.display = "none";
        }
    };


    // typlet
    
    (function start() {
        new TypeIt(".sub-title", {
            spee: 50,
            waitUntilVisible: true,
        })
        .type("고된ㄴ하루의", { delay: 300 })
        .move(-3)
        .delete(1)
        .type(" ")
        .move(null, { to: "END" })
        .type(" 끝을 장식하는")
        .break({ delay: 500 })
        .type("우리의ㅣ", { delay: 300 })
        .delete(1)
        .type(" 음주 기록노트")
        .go();
    })();


    // footer

    const cta = document.querySelector('.cta_header');
    const footer = document.querySelector('.toaster')
    const expandIcon = document.querySelector('.expand_icon')
    const airplaneIcon = document.querySelectorAll('.airplane_icon_wrapper')

    function toggleFooter() {
        footer
            .classList
            .toggle('is_open');
        expandIcon
            .classList
            .toggle('is_reversed')
        Array
            .from(airplaneIcon)
            .map(icon => icon.classList.toggle('is_moving'))
    }

    cta.addEventListener('click', toggleFooter);
    
})();
