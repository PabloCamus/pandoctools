@echo off
:: Predefined:
:: config, user_config, in_ext, out_ext, input_file

if        "%in_ext%"=="" (
    set from=markdown

) else if "%in_ext%"=="md" (
    set from=markdown

) else (
    set from=%in_ext%
)


if        "%out_ext%"=="" (
    set to=markdown
    set t=%to%

) else if "%out_ext%"=="md" (
    set to=markdown
    set t=%to%

) else (
    set to=%out_ext%
    set t=%to%
)


:: stdin from previous operations + Meta-Default.yaml:
set inputs=stdin "%config%\Meta-Default.yaml"
set reader_args=-f "%from%"
set writer_args=-t "%to%" --standalone --self-contained