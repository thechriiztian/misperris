

$(document).ready(function(){
    $("#formularioAdopcion").validate({
        rules:{
            txtCorreo:{
                required:true,
                email:true
            },

            txtRut:{
                required:true,
                number:true,
                minlength:9,
                maxlength:9
            },

            txtNombres:{
                required:true,
                number:false,
            },

            dFecha:{
                date:true,
                min: 1960,
                max:2001
            },

            txtContacto:{
                required:true,
                number:true
            },

            cboRegion:{
                required:true
            },

            cboCiudad:{
                required:true
            },

            cboVivienda:{
                required:true
            }

           /* txtPatente:{
                required:true,
                minlength:3,
                maxlength:10
                //email:true
                //date:true "valida tipo fecha"
            },
            cboMarca:{
                required:true,
            },
            txtAnio:{
                required:true,
                number:true,
                min:1950,
                max:2018
            }*/
        },
        messages:{

            txtCorreo:{
                required:"Debe ingresar un Correo",
                email:"Debe ingresar un Correo Existente"
            },

            txtRut:{
                required:"Ingrese un Rut Valido",
                number:"Ingrese Rut Valido",
                minlength:"Ingrese Rut Valido",
                maxlength:"Ingrese Rut Valido"
            },

            txtNombres:{
                required:"Ingrese nombre valido",
                number:"Ingrese nombre valido",
            },

            dFecha:{
                date:"Ingrese Fecha",
                min:"El año debe ser mayor a 1960",
                max:"El año debe ser menor a 2001"
            },

            txtContacto:{
                required:"Ingrese numero correcto",
                number:"Ingrese numero correcto"
            },

            cboVivienda:{
                required:"Elija una opcion"
            },

            cboCiudad:{
                required:"Elija una opcion"
            },

            cboVivienda:{
                required:"Elija una opcion"
            }

            /*txtPatente:{
                required:"Este campo es Requerido",
                minlength:"Minimo 3 letras",
                maxlength:"Maximo 10 letras"
            },
            cboMarca:{
                required:"Seleccione una Marca"
            },
            txtAnio:{
                required:"Este campo es Requerido",
                number:"Debe ser tipo Numerico",
                min:"Debe ser mayor al año 1950",
                max:"Debe ser menor el año al 2018"
            }*/
        }
    });
});