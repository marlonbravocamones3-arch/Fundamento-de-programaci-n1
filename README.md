# Mesa de Partes Digital en Salud

Prototipo en Python para registrar, validar, buscar y ordenar solicitudes
de atención sanitaria durante emergencias por desastres naturales.
Curso: Fundamentos de Programación (CIIN1205P) - UPN.

## Integrantes
- Marlon Anthony Bravo
- Jose Carlos Altamirano Chircca
- Gian Luka Julder Criollo Jeronimo
- Bryan Roberto Tupac Huaman
- Piero Alexander Untiveros Rodas

## Módulos
- `main.py`: menú principal y registro de datos.
- `validaciones.py`: validación de DNI y gravedad.
- `expedientes.py`: inserción ordenada por prioridad, búsqueda lineal y listado.

## Cómo ejecutar
`python main.py`

## Casos de prueba simples
| Caso | Resultado esperado |
|---|---|
| DNI de 7 dígitos o con letras | Se rechaza y se vuelve a pedir |
| Registrar baja, alta y media | El listado sale: alta, media, baja |
| Buscar `EXP-1001` o su DNI | Muestra la ficha del expediente |
| Buscar `EXP-9999` | "Expediente no encontrado" |
| Listar sin registros | "No hay expedientes registrados" |