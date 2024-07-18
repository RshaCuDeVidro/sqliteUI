# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/sqliteUi_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/sqliteUi_autogen.dir/ParseCache.txt"
  "sqliteUi_autogen"
  )
endif()
