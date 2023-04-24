// Obtener el formulario y el campo de correo electrónico
const form = document.querySelector('form');
const emailInput = document.querySelector('input[name="email"]');

// Agregar evento de escucha al formulario
form.addEventListener('submit', function(event) {
  // Prevenir el envío del formulario
  event.preventDefault();

  // Obtener el valor del campo de correo electrónico
  const emailValue = emailInput.value.trim();

  // Validar el campo de correo electrónico
  if (emailValue === '') {
    // Si el campo está vacío, mostrar mensaje de error
    alert('El campo de correo electrónico no puede estar vacío.');
  } else if (!/^\S+@\S+\.\S+$/.test(emailValue)) {
    // Si el campo no es un correo electrónico válido, mostrar mensaje de error
    alert('Ingrese un correo electrónico válido.');
  } else {
    // Si el campo es válido, enviar el formulario
    form.submit();
  }
});
