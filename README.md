# test_apis_with_python_pytest_unittest_pdoc
Test sobre APIs, del curso de Udemy https://www.udemy.com/course/la-guia-completa-test-de-api-rest-con-python/

Los test fueron modificados por mi, con el fin de practicar y emprolijarlos, orientándolos al paradigma de objetos.

También agregué test nuevos.

**Este repo corresponde a la primer parte del curso, la segunda parte se puede ver acá:** https://github.com/GabrielaVilaro/tests_framework_apis_bdd_gherkin_behave_python_pytest_unittest


**Requisitos**

    Python >= 3.5
    Instalar las dependencias del proyecto: pip3 install -r requirements.txt
    Pycharm

APIs usadas:

NASA: https://api.nasa.gov/

Biblia: https://scripture.api.bible/

Pet Store: https://petstore.swagger.io/

Twiitter: https://developer.twitter.com/ (Se debe solicitar a Twitter permisos para usar sus APIs.)

Se requieren las librerías mencionadas más abajo.

**La documentación completa del proyecto se puede ver abriendo el archivo /docs/tests/index.html en un navegador, haciendo click izquierdo y en "Open Browser" elejir su navegador de preferencia**

<a href="https://ibb.co/RyCLjrW"><img src="https://i.ibb.co/0tfPs43/Screen-Shot-2020-07-19-at-15-09-07.png" alt="Screen-Shot-2020-07-19-at-15-09-07" border="0"></a>

Para generar la documentación usé pdocs3 (está dentro de requirements.txt)  pdoc --html tests

Corriendo allure serve allure_report se genera un reporte de allure framework automático.

<a href="https://ibb.co/fvXdQbB"><img src="https://i.ibb.co/PQrGtR3/Screen-Shot-2020-07-19-at-14-58-53.png" alt="Screen-Shot-2020-07-19-at-14-58-53" border="0"></a>

Y corriendo py.test --alluredir=allure_report ./tests  se puede ver el reposte desde la consola.

EN CURSO DESDE 9/07/2020

El curso incluye: 

  *Postman

  *Curl

  *Python orientado a pruebas de software.

  *Estructuras de datos.

  *Framworks de pruebas con python.

  *Preparacion de entornos Windows

  *Jenkins

  *Pipelines de ejecucion de pruebas.


  Librerías:

  *Pytest,

  *Unittest,

  *Requests,

  *Re (Regular Expressions),

  *Time,

  *json.

  *Allure (para reportes)

  *ObjectPath.


