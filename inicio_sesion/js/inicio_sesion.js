$(document).ready(function() {
    $("#login-form").submit(function(event) {
      // Prevenimos que se realice la acción por defecto del evento submit
      event.preventDefault();
  
      // Obtenemos los valores de los campos de entrada
      var correo = $("#correo").val();
      var pass = $("#pass").val();
  
      // Validamos que los campos no estén vacíos
      if (correo.trim() == "") {
        $("#error-correo").text("Ingrese un correo válido");
        return false;
      } else {
        $("#error-correo").text("");
      }
  
      if (pass.trim() == "") {
        $("#error-pass").text("Ingrese una contraseña válida");
        return false;
      } else {
        $("#error-pass").text("");
      }
  
      // Si la validación es exitosa, enviar formualrio
      $("#login-form")[0].submit();

      window.location.href = '../index.html';
    });
});
  



