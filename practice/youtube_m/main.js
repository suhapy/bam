const moreBnt = document.querySelector('.info .metadata .TitleAndButton .moreBtn');
const title = document.querySelector('.info .metadata .TitleAndButton .title');

moreBnt.addEventListener('click', () => {
    moreBnt.classList.toggle('clicked');
    title.classList.toggle('clamp');
});