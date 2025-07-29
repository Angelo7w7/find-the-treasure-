# Scripts de Base de Datos - AAFTM

Esta carpeta contiene el script SQL esencial para la instalación del sistema AAFTM.

## Archivo Principal

### `ctm_db.sql`
- **Propósito**: Script completo y autosuficiente de la base de datos
- **Uso**: Instalación completa del sistema AAFTM
- **Contiene**: 
  - Estructura completa de todas las tablas
  - Datos iniciales necesarios
  - Índices optimizados
  - Foreign keys y restricciones
  - Sistema de proyectos y tareas
  - Sistema de notificaciones
  - Sistema de recordatorios
  - Sistema de usuarios y preferencias
- **Ejecutar**: Una sola vez durante la instalación inicial

## Instalación

**Para nueva instalación:**
```sql
-- Crear base de datos completa
SOURCE ctm_db.sql;
```

**✅ No se requieren scripts adicionales** - `ctm_db.sql` es completamente autosuficiente.

## Archivos Eliminados

Los siguientes archivos han sido movidos a `backup_obsoletos/` por ser redundantes:
- `add_project_status.sql` - Ya incluido en `ctm_db.sql`
- `email_setup.sql` - Ya incluido en `ctm_db.sql`
- `migration_reminders.sql` - Ya incluido en `ctm_db.sql`
- `Notas del proyecto.md` - Notas de desarrollo ya implementadas
- `reminder_scheduler.php` - Reemplazado por `cron_reminders.php` en raíz
- `resultados.txt` - Archivo temporal de debug
