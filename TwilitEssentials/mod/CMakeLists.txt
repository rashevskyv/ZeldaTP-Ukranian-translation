# Ukrainian language for Twilit Essentials (Dusklight mod).
# -DDUSKLIGHT_DIR=<TwilitRealm/dusklight checkout @ 8b70a4477b8a5331d8bda1bfd6b095c65880c856>
# -DTE_EXAMPLES_DIR=<te-service-examples checkout>  (for include/twilit_essentials/localization.h)
cmake_minimum_required(VERSION 3.26)
project(te_ukrainian CXX)
set(DUSKLIGHT_DIR "" CACHE PATH "Dusklight source tree")
set(TE_EXAMPLES_DIR "" CACHE PATH "te-service-examples checkout")
add_subdirectory("${DUSKLIGHT_DIR}/sdk" dusklight-sdk EXCLUDE_FROM_ALL)
add_mod(te_ukrainian SOURCES src/mod.cpp MOD_JSON src/mod.json RES_DIR res)
target_include_directories(te_ukrainian PRIVATE "${TE_EXAMPLES_DIR}/include")
if (MSVC)
    target_link_options(te_ukrainian PRIVATE "/OPT:NOREF")
    target_compile_options(te_ukrainian PRIVATE /utf-8)
endif ()
