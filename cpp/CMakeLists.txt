# Core C++17 SLAM engine.
#
# For now `vislam` is a header-only INTERFACE target that only exposes the
# public include directory. It becomes a regular library once the first
# implementation files are added under src/.

add_library(vislam INTERFACE)
add_library(vislam::vislam ALIAS vislam)

target_include_directories(vislam INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
target_compile_features(vislam INTERFACE cxx_std_17)

if(VISLAM_BUILD_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()
