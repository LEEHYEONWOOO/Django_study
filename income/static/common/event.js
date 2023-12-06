
$(document).ready(() => {
    var aside_hide_div = document.getElementById('aside_hide_div')
    aside_hide_div.removeEventListener('click', aside_hide_div_event)
    aside_hide_div.addEventListener('click', aside_hide_div_event)

    // 사이드 바 버튼 쿼리셋
    var aside_btn = document.querySelectorAll('.aside_btn')
    // 사이드 바 버튼 클릿 이벤트
    aside_btn.forEach((el) => {
        el.addEventListener('click', () => {
            // 버튼의 다음 태크
            let collapse_div = el.nextElementSibling;
            // 해당 태그를 제외한 다른 태그의 초기화
            $('.aside_collapse').not(collapse_div).removeClass('aside_active').removeAttr('style')
            // 사이드 바 안의 nav_title 스타일 삭제
            $('.nav_title').removeAttr('style')
            // 사이드 바 안의 custom_arrow 스타일 삭제
            $('.custom_arrow').removeAttr('style')
            // 사이드 바 버튼 스타일 삭제
            $(aside_btn).removeAttr('style')
            // collapse_div 의 클래스에 aside_active 가 있으면 aside_active 추가후 if 진행
            if (collapse_div.classList.toggle('aside_active')) {
                // collapse_div 의 자식 태그 포함 높이 측정
                let collapse_height = String(collapse_div.firstElementChild.clientHeight);
                // 높이 적용
                collapse_div.setAttribute('style', 'max-height:' + collapse_height + 'px');
                // 버튼 스타일 적용
                el.setAttribute('style', 'background-color: #796234;')
                // 화살표 스타일 적용
                el.firstElementChild.setAttribute('style', 'transform: rotate(90deg); color: white;');
                // nav_title 스타일 적용
                el.lastElementChild.setAttribute('style', 'font-weight: bold; color: white;')
            }
            else {
                // 열린 버튼을 다시 누른 경우 해당 버튼과 자식 태그 모두 스타일 삭제
                collapse_div.removeAttribute('style');
                el.firstElementChild.removeAttribute('style');
                el.lastElementChild.removeAttribute('style');
            }
        })
    })

    // 사이드 바 메뉴를 열고 안의 노메뉴 클릭 이벤트
    var aside_a = document.querySelectorAll('.aside_a')
    aside_a.forEach((el) => {
        el.addEventListener('click', () => {
            // 모든 스타일 삭제
            $(aside_a).removeAttr('style')
            // 스타일 적용
            el.setAttribute('style', 'font-weight: bold; color: #0d6efd;')
        })
    })

    var tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    var tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
})

function aside_hide_div_event() {
    if (document.getElementById('aside_hide_div').classList.toggle('aside_toggle')) {
            $('#aside').css('left', '0')
        }
        else {
            $('#aside').removeAttr('style')
        }
}

