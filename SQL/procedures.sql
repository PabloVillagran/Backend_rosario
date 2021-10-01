use Proyecto
go
create or alter procedure dbo.administrativo_upsert 	
	@ID_ADMINISTRATIVO int,@ID_USUARIO int	
	as begin 	
	
	if not exists (select 1 from dbo.administrativo where ID_ADMINISTRATIVO=@ID_ADMINISTRATIVO)	
	begin	
	insert dbo.administrativo(ID_USUARIO)	
	select @ID_USUARIO	
	end	
	else	
	begin	
	update dbo.administrativo set 	
	ID_USUARIO=@ID_USUARIO	
	where 0=0	
	and 	
	ID_ADMINISTRATIVO=@ID_ADMINISTRATIVO	
	and 	
	(	
	 coalesce(ID_USUARIO,'') != coalesce(@ID_USUARIO,'') 	
	)	
	end	
	
end	
go

create or alter procedure dbo.alumno_upsert 	
	@ID_ALUMNO int,@ID_USUARIO int	
	as begin 	
	
	if not exists (select 1 from dbo.alumno where ID_ALUMNO=@ID_ALUMNO)	
	begin	
	insert dbo.alumno(ID_USUARIO)	
	select @ID_USUARIO	
	end	
	else	
	begin	
	update dbo.alumno set 	
	ID_USUARIO=@ID_USUARIO	
	where 0=0	
	and 	
	ID_ALUMNO=@ID_ALUMNO	
	and 	
	(	
	 coalesce(ID_USUARIO,'') != coalesce(@ID_USUARIO,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.calificacion_upsert 	
	@ID_CALIFICACION int,@ID_MATRICULA int,@ID_CURSO_MATERIA int,@NOTA decimal(9),@DESCRIPCION varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.calificacion where ID_CALIFICACION=@ID_CALIFICACION)	
	begin	
	insert dbo.calificacion(ID_MATRICULA,ID_CURSO_MATERIA,NOTA,DESCRIPCION)	
	select @ID_MATRICULA,@ID_CURSO_MATERIA,@NOTA,@DESCRIPCION	
	end	
	else	
	begin	
	update dbo.calificacion set 	
	ID_MATRICULA=@ID_MATRICULA,ID_CURSO_MATERIA=@ID_CURSO_MATERIA,NOTA=@NOTA,DESCRIPCION=@DESCRIPCION	
	where 0=0	
	and 	
	ID_CALIFICACION=@ID_CALIFICACION	
	and 	
	(	
	 coalesce(ID_MATRICULA,'') != coalesce(@ID_MATRICULA,'') OR coalesce(ID_CURSO_MATERIA,'') != coalesce(@ID_CURSO_MATERIA,'') OR coalesce(NOTA,'') != coalesce(@NOTA,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.carrera_upsert 	
	@ID_CARRERA int,@CARRERA varchar(100)	
	as begin 	
	
	if not exists (select 1 from dbo.carrera where ID_CARRERA=@ID_CARRERA)	
	begin	
	insert dbo.carrera(CARRERA)	
	select @CARRERA	
	end	
	else	
	begin	
	update dbo.carrera set 	
	CARRERA=@CARRERA	
	where 0=0	
	and 	
	ID_CARRERA=@ID_CARRERA	
	and 	
	(	
	 coalesce(CARRERA,'') != coalesce(@CARRERA,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.curso_upsert 	
	@ID_CURSO int,@CURSO varchar(100),@DESCRIPCION varchar(1000),@ID_SECCION int,@ID_CARRERA int,@ID_GRADO int,@AO int	
	as begin 	
	
	if not exists (select 1 from dbo.curso where ID_CURSO=@ID_CURSO)	
	begin	
	insert dbo.curso(CURSO,DESCRIPCION,ID_SECCION,ID_CARRERA,ID_GRADO,AO)	
	select @CURSO,@DESCRIPCION,@ID_SECCION,@ID_CARRERA,@ID_GRADO,@AO	
	end	
	else	
	begin	
	update dbo.curso set 	
	CURSO=@CURSO,DESCRIPCION=@DESCRIPCION,ID_SECCION=@ID_SECCION,ID_CARRERA=@ID_CARRERA,ID_GRADO=@ID_GRADO,AO=@AO	
	where 0=0	
	and 	
	ID_CURSO=@ID_CURSO	
	and 	
	(	
	 coalesce(CURSO,'') != coalesce(@CURSO,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') OR coalesce(ID_SECCION,'') != coalesce(@ID_SECCION,'') OR coalesce(ID_CARRERA,'') != coalesce(@ID_CARRERA,'') OR coalesce(ID_GRADO,'') != coalesce(@ID_GRADO,'') OR coalesce(AO,'') != coalesce(@AO,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.curso_materia_upsert 	
	@ID_CURSO_MATERIA int,@ID_HORARIO int,@ID_MATERIA int,@ID_CURSO int,@DESCRIPCION varchar(1000),@ID_PROFESOR int	
	as begin 	
	
	if not exists (select 1 from dbo.curso_materia where ID_CURSO_MATERIA=@ID_CURSO_MATERIA)	
	begin	
	insert dbo.curso_materia(ID_HORARIO,ID_MATERIA,ID_CURSO,DESCRIPCION,ID_PROFESOR)	
	select @ID_HORARIO,@ID_MATERIA,@ID_CURSO,@DESCRIPCION,@ID_PROFESOR	
	end	
	else	
	begin	
	update dbo.curso_materia set 	
	ID_HORARIO=@ID_HORARIO,ID_MATERIA=@ID_MATERIA,ID_CURSO=@ID_CURSO,DESCRIPCION=@DESCRIPCION,ID_PROFESOR=@ID_PROFESOR	
	where 0=0	
	and 	
	ID_CURSO_MATERIA=@ID_CURSO_MATERIA	
	and 	
	(	
	 coalesce(ID_HORARIO,'') != coalesce(@ID_HORARIO,'') OR coalesce(ID_MATERIA,'') != coalesce(@ID_MATERIA,'') OR coalesce(ID_CURSO,'') != coalesce(@ID_CURSO,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') OR coalesce(ID_PROFESOR,'') != coalesce(@ID_PROFESOR,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.grado_upsert 	
	@ID_GRADO int,@GRADO varchar(100)	
	as begin 	
	
	if not exists (select 1 from dbo.grado where ID_GRADO=@ID_GRADO)	
	begin	
	insert dbo.grado(GRADO)	
	select @GRADO	
	end	
	else	
	begin	
	update dbo.grado set 	
	GRADO=@GRADO	
	where 0=0	
	and 	
	ID_GRADO=@ID_GRADO	
	and 	
	(	
	 coalesce(GRADO,'') != coalesce(@GRADO,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.horario_upsert 	
	@ID_HORARIO int,@HORA_INICIO time(5),@HORA_FIN time(5),@DESCRIPCION varchar(500)	
	as begin 	
	
	if not exists (select 1 from dbo.horario where ID_HORARIO=@ID_HORARIO)	
	begin	
	insert dbo.horario(HORA_INICIO,HORA_FIN,DESCRIPCION)	
	select @HORA_INICIO,@HORA_FIN,@DESCRIPCION	
	end	
	else	
	begin	
	update dbo.horario set 	
	HORA_INICIO=@HORA_INICIO,HORA_FIN=@HORA_FIN,DESCRIPCION=@DESCRIPCION	
	where 0=0	
	and 	
	ID_HORARIO=@ID_HORARIO	
	and 	
	(	
	 coalesce(HORA_INICIO,'') != coalesce(@HORA_INICIO,'') OR coalesce(HORA_FIN,'') != coalesce(@HORA_FIN,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.materia_upsert 	
	@ID_MATERIA int,@MATERIA varchar(100),@DESCRIPCION varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.materia where ID_MATERIA=@ID_MATERIA)	
	begin	
	insert dbo.materia(MATERIA,DESCRIPCION)	
	select @MATERIA,@DESCRIPCION	
	end	
	else	
	begin	
	update dbo.materia set 	
	MATERIA=@MATERIA,DESCRIPCION=@DESCRIPCION	
	where 0=0	
	and 	
	ID_MATERIA=@ID_MATERIA	
	and 	
	(	
	 coalesce(MATERIA,'') != coalesce(@MATERIA,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.matricula_upsert 	
	@ID_MATRICULA int,@FECHA_INGRESO datetime,@FECHA_EGRESO datetime,@AO int,@ID_ALUMNO int,@NOTAS varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.matricula where ID_MATRICULA=@ID_MATRICULA)	
	begin	
	insert dbo.matricula(FECHA_INGRESO,FECHA_EGRESO,AO,ID_ALUMNO,NOTAS)	
	select @FECHA_INGRESO,@FECHA_EGRESO,@AO,@ID_ALUMNO,@NOTAS	
	end	
	else	
	begin	
	update dbo.matricula set 	
	FECHA_INGRESO=@FECHA_INGRESO,FECHA_EGRESO=@FECHA_EGRESO,AO=@AO,ID_ALUMNO=@ID_ALUMNO,NOTAS=@NOTAS	
	where 0=0	
	and 	
	ID_MATRICULA=@ID_MATRICULA	
	and 	
	(	
	 coalesce(FECHA_INGRESO,'') != coalesce(@FECHA_INGRESO,'') OR coalesce(FECHA_EGRESO,'') != coalesce(@FECHA_EGRESO,'') OR coalesce(AO,'') != coalesce(@AO,'') OR coalesce(ID_ALUMNO,'') != coalesce(@ID_ALUMNO,'') OR coalesce(NOTAS,'') != coalesce(@NOTAS,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.matricula_curso_upsert 	
	@ID_MATRICULA_CURSO int,@ID_MATRICULA int,@ID_CURSO int,@NOTAS varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.matricula_curso where ID_MATRICULA_CURSO=@ID_MATRICULA_CURSO)	
	begin	
	insert dbo.matricula_curso(ID_MATRICULA,ID_CURSO,NOTAS)	
	select @ID_MATRICULA,@ID_CURSO,@NOTAS	
	end	
	else	
	begin	
	update dbo.matricula_curso set 	
	ID_MATRICULA=@ID_MATRICULA,ID_CURSO=@ID_CURSO,NOTAS=@NOTAS	
	where 0=0	
	and 	
	ID_MATRICULA_CURSO=@ID_MATRICULA_CURSO	
	and 	
	(	
	 coalesce(ID_MATRICULA,'') != coalesce(@ID_MATRICULA,'') OR coalesce(ID_CURSO,'') != coalesce(@ID_CURSO,'') OR coalesce(NOTAS,'') != coalesce(@NOTAS,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.pago_upsert 	
	@ID_PAGO int,@MONTO decimal(9),@DESCRIPCION varchar(1000),@ID_MATRICULA int,@ID_TIPO_PAGO int,@FECHA_VENCIMIENTO datetime,@FECHA_PAGO datetime	
	as begin 	
	
	if not exists (select 1 from dbo.pago where ID_PAGO=@ID_PAGO)	
	begin	
	insert dbo.pago(MONTO,DESCRIPCION,ID_MATRICULA,ID_TIPO_PAGO,FECHA_VENCIMIENTO,FECHA_PAGO)	
	select @MONTO,@DESCRIPCION,@ID_MATRICULA,@ID_TIPO_PAGO,@FECHA_VENCIMIENTO,@FECHA_PAGO	
	end	
	else	
	begin	
	update dbo.pago set 	
	MONTO=@MONTO,DESCRIPCION=@DESCRIPCION,ID_MATRICULA=@ID_MATRICULA,ID_TIPO_PAGO=@ID_TIPO_PAGO,FECHA_VENCIMIENTO=@FECHA_VENCIMIENTO,FECHA_PAGO=@FECHA_PAGO	
	where 0=0	
	and 	
	ID_PAGO=@ID_PAGO	
	and 	
	(	
	 coalesce(MONTO,'') != coalesce(@MONTO,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') OR coalesce(ID_MATRICULA,'') != coalesce(@ID_MATRICULA,'') OR coalesce(ID_TIPO_PAGO,'') != coalesce(@ID_TIPO_PAGO,'') OR coalesce(FECHA_VENCIMIENTO,'') != coalesce(@FECHA_VENCIMIENTO,'') OR coalesce(FECHA_PAGO,'') != coalesce(@FECHA_PAGO,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.profesor_upsert 	
	@ID_PROFESOR int,@ID_USUARIO int	
	as begin 	
	
	if not exists (select 1 from dbo.profesor where ID_PROFESOR=@ID_PROFESOR)	
	begin	
	insert dbo.profesor(ID_USUARIO)	
	select @ID_USUARIO	
	end	
	else	
	begin	
	update dbo.profesor set 	
	ID_USUARIO=@ID_USUARIO	
	where 0=0	
	and 	
	ID_PROFESOR=@ID_PROFESOR	
	and 	
	(	
	 coalesce(ID_USUARIO,'') != coalesce(@ID_USUARIO,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.seccion_upsert 	
	@ID_SECCION int,@SECCION varchar(100)	
	as begin 	
	
	if not exists (select 1 from dbo.seccion where ID_SECCION=@ID_SECCION)	
	begin	
	insert dbo.seccion(SECCION)	
	select @SECCION	
	end	
	else	
	begin	
	update dbo.seccion set 	
	SECCION=@SECCION	
	where 0=0	
	and 	
	ID_SECCION=@ID_SECCION	
	and 	
	(	
	 coalesce(SECCION,'') != coalesce(@SECCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.tipo_pago_upsert 	
	@ID_TIPO_PAGO int,@TIPO_PAGO varchar(300),@DESCRIPCION varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.tipo_pago where ID_TIPO_PAGO=@ID_TIPO_PAGO)	
	begin	
	insert dbo.tipo_pago(TIPO_PAGO,DESCRIPCION)	
	select @TIPO_PAGO,@DESCRIPCION	
	end	
	else	
	begin	
	update dbo.tipo_pago set 	
	TIPO_PAGO=@TIPO_PAGO,DESCRIPCION=@DESCRIPCION	
	where 0=0	
	and 	
	ID_TIPO_PAGO=@ID_TIPO_PAGO	
	and 	
	(	
	 coalesce(TIPO_PAGO,'') != coalesce(@TIPO_PAGO,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.tipo_usuario_upsert 	
	@ID_TIPO_USUARIO int,@TIPO_USUARIO varchar(100),@DESCRIPCION varchar(1000)	
	as begin 	
	
	if not exists (select 1 from dbo.tipo_usuario where ID_TIPO_USUARIO=@ID_TIPO_USUARIO)	
	begin	
	insert dbo.tipo_usuario(TIPO_USUARIO,DESCRIPCION)	
	select @TIPO_USUARIO,@DESCRIPCION	
	end	
	else	
	begin	
	update dbo.tipo_usuario set 	
	TIPO_USUARIO=@TIPO_USUARIO,DESCRIPCION=@DESCRIPCION	
	where 0=0	
	and 	
	ID_TIPO_USUARIO=@ID_TIPO_USUARIO	
	and 	
	(	
	 coalesce(TIPO_USUARIO,'') != coalesce(@TIPO_USUARIO,'') OR coalesce(DESCRIPCION,'') != coalesce(@DESCRIPCION,'') 	
	)	
	end	
	
	end	
go

create or alter procedure dbo.usuario_upsert 	
	@ID_USUARIO int,@USUARIO varchar(100),@NOMBRES varchar(500),@APELLIDOS varchar(500),@TELEFONO varchar(100),@EMAIL varchar(300),@ID_TIPO_USUARIO int,@DOMICILIO varchar(1000),@PASSWORD varchar(300)	
	as begin 	
	
	if not exists (select 1 from dbo.usuario where ID_USUARIO=@ID_USUARIO)	
	begin	
	insert dbo.usuario(USUARIO,NOMBRES,APELLIDOS,TELEFONO,EMAIL,ID_TIPO_USUARIO,DOMICILIO,PASSWORD)	
	select @USUARIO,@NOMBRES,@APELLIDOS,@TELEFONO,@EMAIL,@ID_TIPO_USUARIO,@DOMICILIO,@PASSWORD	
	end	
	else	
	begin	
	update dbo.usuario set 	
	USUARIO=@USUARIO,NOMBRES=@NOMBRES,APELLIDOS=@APELLIDOS,TELEFONO=@TELEFONO,EMAIL=@EMAIL,ID_TIPO_USUARIO=@ID_TIPO_USUARIO,DOMICILIO=@DOMICILIO,PASSWORD=@PASSWORD	
	where 0=0	
	and 	
	ID_USUARIO=@ID_USUARIO	
	and 	
	(	
	 coalesce(USUARIO,'') != coalesce(@USUARIO,'') OR coalesce(NOMBRES,'') != coalesce(@NOMBRES,'') OR coalesce(APELLIDOS,'') != coalesce(@APELLIDOS,'') OR coalesce(TELEFONO,'') != coalesce(@TELEFONO,'') OR coalesce(EMAIL,'') != coalesce(@EMAIL,'') OR coalesce(ID_TIPO_USUARIO,'') != coalesce(@ID_TIPO_USUARIO,'') OR coalesce(DOMICILIO,'') != coalesce(@DOMICILIO,'') OR coalesce(PASSWORD,'') != coalesce(@PASSWORD,'') 	
	)	
	end	
	
	end	
go

USE Proyecto
go
create or alter trigger dbo.Calificacion_Audit
On  dbo.calificacion
After Update, Delete
Not For Replication
As
Begin
    If (Select COUNT(*) From inserted) > 0
    Begin
        Insert Into Proyecto_Audit.dbo.calificacion (ID_CALIFICACION,ID_MATRICULA,ID_CURSO_MATERIA,NOTA,DESCRIPCION,AuditDB_AuditType,AuditDB_AuditDate,AuditDB_AuditUser,AuditDB_AuditLogin)
		Select ID_CALIFICACION,ID_MATRICULA,ID_CURSO_MATERIA,NOTA,DESCRIPCION,'U',AuditDB_AuditDate,AuditDB_AuditUser,AuditDB_AuditLogin From deleted
    End
    Else If (Select COUNT(*) From deleted) > 0
    Begin
		 Insert Into Proyecto_Audit.dbo.calificacion (ID_CALIFICACION,ID_MATRICULA,ID_CURSO_MATERIA,NOTA,DESCRIPCION,AuditDB_AuditType,AuditDB_AuditDate,AuditDB_AuditUser,AuditDB_AuditLogin)
		Select ID_CALIFICACION,ID_MATRICULA,ID_CURSO_MATERIA,NOTA,DESCRIPCION,'D',AuditDB_AuditDate,AuditDB_AuditUser,AuditDB_AuditLogin From deleted
    End
End
go