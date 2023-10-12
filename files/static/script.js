function toggleModal() {
    let modal = document.querySelector('.modal')
    modal.classList.toggle('is-active')
}

function deleteItem(pk) {
    document.cookie = 'pk=' + pk
    toggleModal()
}

document.querySelector('.menu-btn').addEventListener("click", function(e) {
    e.preventDefault();
    document.querySelector('.menu').classList.toggle('menu_active');
  })
