console.log('집에 가고 싶어!');
// console.log로 제대로 입력됐는지 확인할 수 있다.
// const checkbox=document.getElementById('checkbox');
const checkbox=document.querySelector('.checkbox');
console.log(checkbox);

checkbox.addEventListener('click',toggleClick);
// 내가 checkbox를 click하면 함수 click(내가 설정하는 것)을 불러온다.
function click() {
    if(document.body.classList.contains('dark')){
        document.body.classList.remove('dark');
        console.log('convert into Light Mode');
    }else{
        document.body.classList.add('dark')
        console.log('convert into Dark Mode');
    }
}
// 클릭함수//  body.옆에 있는 얘기 dark를 포함하고 있다면 없애주라, dark가 원래부터 없으면 다크를 추가해라.
//toggle
function toggleClick() {
    document.body.classList.toggle('dark');
    console.log('Working!');
}