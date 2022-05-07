const icono  = document.querySelector('.imagenmenu'); 
const menu = document.querySelector('.navegation');

console.log(icono)
console.log(menu)

icono.addEventListener('click', () =>{
    menu.classList.toggle("spread")
})