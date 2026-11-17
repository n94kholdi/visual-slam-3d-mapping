cmake_minimum_required(VERSION 3.22)

project(vislam
  VERSION 0.1.0
  DESCRIPTION "Offline smartphone-based Visual-Inertial SLAM (iPhone 13 RGB + IMU)"
  LANGUAGES CXX
)

# -----------------------------------------------------------------------------
# Global C++ settings
# -----------------------------------------------------------------------------
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING "Build type" FORCE)
endif()

# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------
option(VISLAM_BUILD_TESTS "Build GoogleTest unit/integration tests" ON)
option(VISLAM_WARNINGS_AS_ERRORS "Treat compiler warnings as errors" OFF)

# Shared warning flags, applied per-target via vislam_set_warnings().
function(vislam_set_warnings target)
  target_compile_options(${target} PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -Wshadow -Wconversion>
    $<$<AND:$<CXX_COMPILER_ID:GNU,Clang>,$<BOOL:${VISLAM_WARNINGS_AS_ERRORS}>>:-Werror>
  )
endfunction()

# -----------------------------------------------------------------------------
# Dependencies
# -----------------------------------------------------------------------------
# Third-party dependencies (Eigen3 >= 3.4, OpenCV >= 4.5, yaml-cpp, spdlog,
# Ceres >= 2.1 / GTSAM >= 4.1, DBoW2/3) are added with find_package() in the
# phase that first needs them. The Ceres-vs-GTSAM choice will be recorded as an
# ADR in docs/decisions/ before it is linked.

# -----------------------------------------------------------------------------
# Subprojects
# -----------------------------------------------------------------------------
add_subdirectory(cpp)
