@echo off
:: May be useful:
:: %call% setvar scripts %r% where $PATH:panfl.exe
:: set scripts=%scripts:~0,-10%
:: (or use `scripts` var predefined in pandoctools.exe)

:: `panfl sugartex -t %t%` = `sugartex %t%`
:: `panfl sugartex_kiwi` = `sugartex --kiwi`

:: Predefined:
:: config, user_config, in_ext, out_ext, input_file

%r% cat-md stdin | ^
%r% pre-knitty %input_file% | ^
%r% pre-sugartex | ^
%r% cat-md %inputs% | ^
%r% pandoc %reader_args% -t json | ^
%r% knitty %input_file% %reader_args% %writer_args% | ^
%r% sugartex %to% | ^
%r% pandoc-crossref %to% | ^
%r% pandoc -f json %writer_args%
