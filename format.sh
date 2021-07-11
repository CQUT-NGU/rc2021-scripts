#!/usr/bin/env bash

main='Core/Src/main.c'

find $main $@ -regex '.*\.\(cpp\|hpp\|c\|h\)' -exec clang-format --verbose -style=file -i {} \;
