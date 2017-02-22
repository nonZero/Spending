"use strict";

console.log('start');

$("p").click(function () {
    console.log('click');
    let el = $(this);
    el.next().html(el.html() + "!");
    el.after($("<p>shalom</p>"));
});

console.log('end');
