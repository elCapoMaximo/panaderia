$(function() {
  $(".cod-form").submit(function(event) {
    event.preventDefault(); // previene el envío del formulario

    var correo = $("#reg-correo").val();
    var contrasenia = $("#reg-pass").val();
    var confirmarContrasenia = $("#reg-rep-pass").val();

    // Validamos que los campos no estén vacíos y que las contraseñas coincidan
    if (correo.trim() == "") {
      $("#error-correo").text("Ingrese un correo válido");
      return false;
    } else {
      $("#error-correo").text("");
    }

    if (contrasenia.trim() == "" || confirmarContrasenia.trim() == "") {
      $("#error-contrasenia").text("Ambas contraseñas deben estar completas");
      if (contrasenia != confirmarContrasenia) {
        $("#error-confirmar-contrasenia").text("Las contraseñas no puede estar en Blanco");
        return false;
      } else {
        $("#error-confirmar-contrasenia").text("");
      }
  
      return false;
    } else {
      $("#error-contrasenia").text("");
    }

    
    if (contrasenia != confirmarContrasenia) {
      $("#error-confirmar-contrasenia").text("Las contraseñas no coinciden");
      return false;
    } else {
      $("#error-confirmar-contrasenia").text("");
    }

    
    $(this).unbind("submit").submit();
    window.location.href = homeUrl;
  });
});
