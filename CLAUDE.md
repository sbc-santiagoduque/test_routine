# test_routine

Repositorio de demostración de rutinas de Claude Code. Código inventado: una
función que suma horas hábiles para calcular el vencimiento de un ANS.

## Cómo se prueba

```
python -m unittest -v
```

Solo `unittest` de la librería estándar. No hay dependencias.

## Lista de revisión de un PR

Al revisar un pull request, comprobar cada punto y citar archivo y línea:

1. **Identificadores en inglés.** Variables, funciones, clases y archivos nuevos en inglés. Los comentarios pueden ir en español.
2. **Horas con zona.** Nada de `datetime.now()` ni `datetime(...)` sin zona horaria. Todo `datetime` que entra a `sla.py` debe tener `tzinfo`.
3. **Pruebas.** Todo comportamiento nuevo trae su prueba en `test_sla.py`, con `unittest` (no `pytest`). Las pruebas existentes deben seguir pasando.
4. **Sin salidas de depuración.** Nada de `print` en el código de `sla.py`.
5. **Sin nombres de personas** en el código ni en las pruebas.

El comentario de revisión termina con un veredicto: **Aprobado** o **Requiere cambios**, y la salida de las pruebas.
