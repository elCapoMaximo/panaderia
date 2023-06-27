// Obtener el formulario y los campos
const formulario = document.getElementById("formulario-contacto");
const nombre = formulario.elements["nombre"];
const email = formulario.elements["email"];
const mensaje = formulario.elements["mensaje"];

// Obtener los elementos de error
const errorNombre = document.getElementById("error-nombre");
const errorEmail = document.getElementById("error-email");
const errorMensaje = document.getElementById("error-mensaje");

// Función para validar un campo y mostrar un mensaje de error si es necesario
function validarCampo(campo, error, mensajeError) {
  if (campo.value.trim() === "") {
    error.innerHTML = mensajeError;
    return false;
  } else {
    error.innerHTML = "";
    return true;
  }
}

// Validar el formulario cuando se envía
formulario.addEventListener("submit", function(event) {
  // Validar cada campo
  const esNombreValido = validarCampo(nombre, errorNombre, "Debes ingresar tu nombre");
  const esEmailValido = validarCampo(email, errorEmail, "Debes ingresar tu correo electrónico");
  const esEmailFormatoValido = /\S+@\S+\.\S+/.test(email.value.trim());
  const esMensajeValido = validarCampo(mensaje, errorMensaje, "Debes ingresar un mensaje");

  // Si algún campo no es válido, prevenir el envío del formulario
  if (!esNombreValido || !esEmailValido || !esEmailFormatoValido || !esMensajeValido) {
    event.preventDefault();
  }
});
