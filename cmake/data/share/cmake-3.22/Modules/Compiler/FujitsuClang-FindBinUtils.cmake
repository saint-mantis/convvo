if(NOT DEFINED _CMAKE_PROCESSING_LANGUAGE OR _CMAKE_PROCESSING_LANGUAGE STREQUAL "")
  message(FATAL_ERROR "Internal error: _CMAKE_PROCESSING_LANGUAGE is not set")
endif()

set(CMAKE_${_CMAKE_PROCESSING_LANGUAGE}_COMPILER_AR ar)
set(CMAKE_${_CMAKE_PROCESSING_LANGUAGE}_COMPILER_RANLIB ranlib)
