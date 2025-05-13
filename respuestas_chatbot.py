from datetime import datetime
import random

# Obtiene la respuesta basada en la intención detectada
def ObtenerRespuesta(ListaIntentos, JsonIntentos):
    if not ListaIntentos or ListaIntentos[0]['Intencion'] == 'unknown':
        return ["Lo siento, no tengo información sobre ese tema. ¿Puedes preguntar algo más relacionado con el hospital?"]
    
    Ayuda = "¿En qué más te puedo ayudar?"
    InfoContacto = 'Si necesitas más información, no dudes en comunicarte a nuestros canales oficiales.\n<b>Correo: </b> <a href="mailto:alianzaestrategica@hps.org.mx"><button class="info">alianzaestrategica@hps.org.mx ✉️</button></a>\n<b>Teléfono Principal y Extensiones:\n</b> <a href="tel:6677126606"><button class="info">6677126606 📞</button></a><b> </b><a href="EXTENCIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>'
    TelefonoPrincipal = '<b>Teléfono Principal y Extensión</b> \n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'

    Etiqueta = ListaIntentos[0]['Intencion']    
    
    for Intento in JsonIntentos['intents']:
        if Intento['tag'] == Etiqueta:
            # Se elige una respuesta aleatoria
            Respuesta = random.choice(Intento['respuestas'])

            # Comparar directamente con el tag en lugar de la respuesta
            if Intento['tag'] == "fecha":
                FechaActual = datetime.now().strftime("%A, %d de %B del %Y")
                return [f"Hoy es {FechaActual}", Ayuda]
            elif Intento['tag'] == "hora":
                HoraActual = datetime.now().strftime("%H:%M")
                return [f"Son las {HoraActual}", Ayuda]
            elif Intento['tag'] == "logo":
                return [
                    Respuesta,
                    '<a href="https://hospitalpediatrico.org/oficial/" target="_blank"><img class="elemento_interno" decoding="async" width="100" src="https://hospitalpediatrico.org/oficial/wp-content/uploads/2022/08/icon-logo-hps.png" alt="Hospital Pediátrico de Sinaloa"></a>'
                ]
            elif Intento['tag'] == "informacion_general":
                return [
                    Respuesta,
                    InfoContacto
                ]
            elif Intento['tag'] == "ubicacion":
                return [
                    Respuesta,
                    '<iframe class="elemento_interno" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3621.9029951692764!2d-107.40199942463111!3d24.79877497796962!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86bcd0b34e811d65%3A0x7728b9f1122455ed!2sHospital%20Pedi%C3%A1trico%20de%20Sinaloa!5e0!3m2!1ses!2smx!4v1743604900818!5m2!1ses!2smx" width="300" height="200" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
                    Ayuda
                ]
            elif Intento['tag'] == "especialidades":
                return [
                    Respuesta,
                    'Selecciona una especialidad para saber más información'
                    '\n<button class="info" onclick="Mostrar(\'Alergologia\')">Alergologia</button><b> </b><button class="info" onclick="Mostrar(\'Cardiologia\')">Cardiologia</button><b> </b><button class="info" onclick="Mostrar(\'Cardiologia\')">Cirugia cardiovascular</button>'
                    '\n<button class="info" onclick="Mostrar(\'Cirugia\')">Cirugia general</button><b> </b><button class="info" onclick="Mostrar(\'Cirugia\')">Cirugia plastica</button><b> </b><button class="info" onclick="Mostrar(\'Clinica de obesidad\')">Clinica de obesidad</button>'
                    '\n<button class="info" onclick="Mostrar(\'Comunicacion humana\')">Comunicacion humana</button><b> </b><button class="info" onclick="Mostrar(\'Cons. de urgencias\')">Cons. de urgencias</button><b> </b><button class="info" onclick="Mostrar(\'Consulta externa\')">Consulta externa</button>'
                    '\n<button class="info" onclick="Mostrar(\'Dermatologia\')">Dermatologia</button><b> </b><button class="info" onclick="Mostrar(\'Endocrinologia\')">Endocrinologia</button><b> </b><button class="info" onclick="Mostrar(\'Estomatologia\')">Estomatologia</button>'
                    '\n<button class="info" onclick="Mostrar(\'Foniatria y audiologia\')">Foniatria y audiologia</button><b> </b><button class="info" onclick="Mostrar(\'Gastroenterologia\')">Gastroenterologia</button><b> </b><button class="info" onclick="Mostrar(\'Genetica\')">Genetica</button>'
                    '\n<button class="info" onclick="Mostrar(\'Hematologia\')">Hematologia</button><b> </b><button class="info" onclick="Mostrar(\'Infectologia\')">Infectologia</button><b> </b><button class="info" onclick="Mostrar(\'Medicina fisica y rehabilitacion\')">Medicina fisica y rehabilitacion</button>'
                    '\n<button class="info" onclick="Mostrar(\'Medicina interna\')">Medicina interna</button><b> </b><button class="info" onclick="Mostrar(\'Nefrologia\')">Nefrologia</button><b> </b><button class="info" onclick="Mostrar(\'Neonatologia\')">Neonatologia</button>'
                    '\n<button class="info" onclick="Mostrar(\'Neumologia\')">Neumologia</button><b> </b><button class="info" onclick="Mostrar(\'Neurologia\')">Neurologia</button><b> </b><button class="info" onclick="Mostrar(\'Neurocirugia\')">Neurocirugia</button>'
                    '\n<button class="info" onclick="Mostrar(\'Nutricion\')">Nutricion</button><b> </b><button class="info" onclick="Mostrar(\'Oftalmologia\')">Oftalmologia</button><b> </b><button class="info" onclick="Mostrar(\'Oncologia\')">Oncologia</button>'
                    '\n<button class="info" onclick="Mostrar(\'Ortodoncia\')">Ortodoncia</button><b> </b><button class="info" onclick="Mostrar(\'Otorrinolaringologia\')">Otorrinolaringologia</button><b> </b><button class="info" onclick="Mostrar(\'Psicologia\')">Psicologia</button>'
                    '\n<button class="info" onclick="Mostrar(\'Traumatologia y ortopedia\')">Traumatologia y ortopedia</button><b> </b><button class="info" onclick="Mostrar(\'Urologia\')">Urologia</button>',
                    InfoContacto
                ]
            elif Intento['tag'] == "pagina_web":
                return [
                    Respuesta,
                    '<button class="info" onclick="window.open(\'https://hospitalpediatrico.org/oficial/\', \'_blank\');">Pagina Web Oficial ➡️➡️🌐</button>'
                ]
            elif Intento['tag'] == "info_chatbot":
                return [
                    Respuesta,
                    "Estoy aquí para responder tus preguntas relacionadas con el hospital."
                ]
            elif Intento['tag'] == "telefono":
                return [
                    '<b>Teléfono Principal y Extensiones:</b>'
                    '\n<a href="tel:6677126606"><button class="info">667 712 66 06 📞</button></a>'
                    '<b> </b><a href="EXTENCIONES.pdf" target="_blank"><button class="archivo" style="margin-bottom: 5px;">Todas las Extensiones ➡️</button></a>'+
                    Respuesta,
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Otros Teléfonos:</b>'
                    '\n<a href="tel:6677139004"><button class="info">667 713 90 04 📞</button></a>'
                    '<b> </b><a href="tel:6677126607"><button class="info">667 712 66 07 📞</button></a>'
                    '\n<a href="tel:6677126608"><button class="info">667 712 66 08 📞</button></a>'
                    '<b> </b><a href="tel:6677133523"><button class="info">667 713 35 23 📞</button></a>'
                    '\n<a href="tel:6672612200"><button class="info">667 261 22 00 📞</button></a>'
                ]
            elif Intento['tag'] == "correo":
                return [
                    Respuesta + '\n<a href="mailto:alianzaestrategica@hps.org.mx"><button class="info">alianzaestrategica@hps.org.mx ✉️</button></a>'
                ]
            elif Intento['tag'] == "donaciones":
                return [
                    Respuesta,
                    InfoContacto
                ]
            elif Intento['tag'] == "redes_sociales":
                return [
                    Respuesta,
                    '<b>Redes Sociales Oficiales:</b>'
                    '\n<button class="info" style="background-color:#1877f2;" onclick="window.open(\'https://www.facebook.com/profile.php?id=100083151401330\', \'_blank\');"><i class="fab fa-facebook"></i> Facebook</button> '
                    '<b> </b><button class="info" style="background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);" onclick="window.open(\'https://www.instagram.com/hospitalpediatricodesinaloa?igsh=MTVvZmkxZ25obTMybw%3D%3D\', \'_blank\');"><i class="fab fa-instagram"></i> Instagram</button> '
                    '<b> </b><button class="info" style="background-color: black" onclick="window.open(\'https://x.com/pediatrico\', \'_blank\');"><i class="fab fa-twitter"></i> Twitter</button>'
                ]
            elif Intento['tag'] == "extensiones":
                return [
                    Respuesta +
                    '\n<a href="EXTENCIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>',
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Teléfono Principal:</b>'
                    '\n<a href="tel:6677126606"><button class="info">667 712 66 06 📞</button></a>',
                    '<img class="elemento_interno" src="P1.png" alt="Ext. P1">'
                ]
            elif Intento['tag'] == "farmacia":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p><b>Farmacia 💊</b>     <b class="color">  Planta Baja</b></p>'
                        '</header>'
                        '<main>'
                            '<p>María Conchita Calderón Romero</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    '<b>Telefono Principal y Extensiones</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7041"><button class="archivo"><b>Farmacia: </b>7041</button></a>'
                    '<b> </b><a href="tel:6677126606,7042"><button class="archivo"><b>Farmacia Oficina: </b>7042</button></a>'
                ]
            elif Intento['tag'] == "alianza_estrategica":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Alianza Estratégica 🙏</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>María Conchita Calderón Romero</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7004"><button class="archivo"><b>Alianza Estratégica: </b>7004</button></a>'
                ]
            elif Intento['tag'] == "almacen_general":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Almacén General y Activos fijos 💉</b>     <b class="color">  Planta baja</b></p>'
                        '</header>'
                        '<main>'
                            '<p>C. Olga Lucero Pimental Labrada</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7005"><button class="archivo"><b>Almacén General: </b>7005</button></a>'
                ]
            elif Intento['tag'] == "sub_almacen":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Sub Almacén 💉</b>     <b class="color">  Piso 5</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7006"><button class="archivo"><b>Sub Almacén: </b>7006</button></a>'
                ]
            elif Intento['tag'] == "apoyo_nutricional":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b class="emoji">Apoyo Nutricional 🍎</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7007"><button class="archivo"><b>Apoyo Nutricional: </b>7007</button></a>'
                ]
            elif Intento['tag'] == "archivo_clinico":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Archivo Clínico 📂</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Lic. Dalia Ramírez Morales</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7008"><button class="archivo"><b>Archivo Clínico: </b>7008</button></a>'
                ]
            elif Intento['tag'] == "aula_capacitacion":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Aula de Capacitación 🧑‍🏫</b>     <b class="color">  Piso</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Maricruz</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7010"><button class="archivo"><b>Aula de Capacitación: </b>7010</button></a>'
                ]
            elif Intento['tag'] == "biomedica_ingenieria":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Biomédica Ingeniería 🔩</b>     <b class="color">  Piso 1</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Ing. Sinhue Everardo Acosta Osuna</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7011"><button class="archivo"><b>Biomédica Ingeniería: </b>7011</button></a>'
                ]
            elif Intento['tag'] == "calidad":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Calidad Hospitalaria 🏥</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Enf. Fabiola Sánchez Mapula</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7012"><button class="archivo"><b>Calidad Hospitalaria: </b>7012</button></a>'
                ]
            elif Intento['tag'] == "cardiologia":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Cardiología 🫀</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Dr. José Antonio Quibrera Matienzo</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7013"><button class="archivo"><b>Cardiología: </b>7013</button></a>'
                ]
            elif Intento['tag'] == "mision_vision":   
                return [
                    "<b>Mision y Vision</b>\nLa mision y vision del Hospital Pediatrico de Sinaloa reflejan nuestro compromiso con la salud infantil y el desarrollo de la medicina pediatrica en Mexico.",
                    Respuesta,
                    '<b>Vision:</b> Ser un hospital líder a nivel nacional en atención pediátrica, formación médica e investigación, con personal suficiente y capacitado.'                
                ]
            elif Intento['tag'] == "central_de_cuentas":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Central de Cuentas 📋</b>     <b class="color">  Piso </b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7014"><button class="archivo"><b>Central de Cuentas: </b>7014</button></a>'
                ]
            elif Intento['tag'] == "centro_mezclas":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Centro de Mezclas 💉</b>     <b class="color">  Piso</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado] </p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7015"><button class="archivo"><b>Centro de Mezclas: </b>7015</button></a>'
                ]
            elif Intento['tag'] == "ceye":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>CEYE (Central de Equipos y Esterilización) 🥼</b>     <b class="color">  Piso 5</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Enf. Rosa Esthela Robles Uriarte</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7016"><button class="archivo"><b>CEYE: </b>7016</button></a>'
                ]
            elif Intento['tag'] == "cirugia":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Cirugía 🩺</b>     <b class="color">  Piso</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Dr. Juan Manuel Zazueta Tirado</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    '<b>Teléfono Principal y Extensiones</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7017"><button class="archivo"><b>Cirugía: </b>7017</button></a>'
                    '<b> </b><a href="tel:6677126606,7018"><button class="archivo"><b>Cirugía Oficina: </b>7018</button></a>'
                ]
            elif Intento['tag'] == "clinica_heridas":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Clínica de Heridas 🤕</b>     <b class="color">  Piso</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Enf. María Consuelo Chacón Zapién</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7019"><button class="archivo"><b>Clinica de Heridas: </b>7019</button></a>'
                ]
            elif Intento['tag'] == "cobranza":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Cobranza 💸</b>     <b class="color">  Piso</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7020"><button class="archivo"><b>Cobranza: </b>7020</button></a>'
                ]
            elif Intento['tag'] == "cocina":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Cocina 🍽️</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7021"><button class="archivo"><b>Cocina: </b>7021</button></a>'
                ]
            elif Intento['tag'] == "consulta_externa":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Consulta Externa 🧑‍⚕️</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Dra. Aleida López Barajas</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    '<b>Teléfono Principal y Extensiones</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7023"><button class="archivo"><b>Consulta Externa Recepción: </b>7023</button></a>'
                    '<b> </b><a href="tel:6677126606,7120"><button class="archivo"><b>Consulta Externa Jefe Pediátrico: </b>7120</button></a>'
                ]
            elif Intento['tag'] == "contabilidad_oficina":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Contabilidad 💰</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7024"><button class="archivo"><b>Contabilidad: </b>7024</button></a>'
                ]
            elif Intento['tag'] == "dental":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Estomatología y Ortodoncia 🦷</b>     <b class="color">  Piso 2</b></p>'
                        '</header>'
                        '<main>'
                            '<p>Dra. Raquel Salazar Márquez</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7026"><button class="archivo"><b>Estomatología y Ortodoncia: </b>7026</button></a>'
                ]
            elif Intento['tag'] == "enfermeria_ensenanza":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Enfermería Enseñanza ✏️</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7029"><button class="archivo"><b>Enfermería Enseñanza: </b>7029</button></a>'
                ]
            elif Intento['tag'] == "enfermeria_jefatura":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Enfermería Jefatura 👩‍⚕️</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    '<b>Teléfono Principal y Extensiones</b>'
                    '\n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'
                    '<b> </b><a href="tel:6677126606,7030"><button class="archivo"><b>Enfermería Jefatura: </b>7030</button></a>'
                    '<b> </b><a href="tel:6677126606,7031"><button class="archivo"><b>Enfermería Jefatura Secretaria: </b>7031</button></a>'
                ]
            elif Intento['tag'] == "enfermeria_subjefatura":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Enfermería Subjefatura 👩‍⚕️</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7032"><button class="archivo"><b>Enfermería Subjefatura: </b>7032</button></a>'
                ]
            elif Intento['tag'] == "ensenanza_dos":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Enseñanza Dos 📚</b>     <b class="color">  Piso 6</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>', 
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7033"><button class="archivo"><b>Enseñanza Dos: </b>7033</button></a>'
                ]
            elif Intento['tag'] == "ensenanza_investigacion":
                return [
                    '<section class="card">'
                        '<header>'
                            '<p ><b>Enseñanza Investigación 📖</b>     <b class="color">  Piso 4</b></p>'
                        '</header>'
                        '<main>'
                            '<p>[Nombre del Encargado]</p>'
                        '</main>'
                    '</section>',
                    Respuesta,
                    TelefonoPrincipal+
                    '<b> </b><a href="tel:6677126606,7034"><button class="archivo"><b>Enseñanza e Investigación: </b>7034</button></a>'
                ]
            return [Respuesta]
    
    return ["Lo siento, no entendí tu pregunta."]
