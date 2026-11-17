# GoogleTest unit & integration tests.
#
# Test targets are registered here as modules are implemented, e.g.:
#
#   add_executable(test_rotation test_rotation.cpp)
#   target_link_libraries(test_rotation PRIVATE vislam::vislam GTest::gtest_main)
#   vislam_set_warnings(test_rotation)
#   gtest_discover_tests(test_rotation)

find_package(GTest QUIET)

if(NOT GTest_FOUND)
  message(STATUS "GoogleTest not found - C++ tests will not be built "
                 "(install libgtest-dev or set -DVISLAM_BUILD_TESTS=OFF).")
  return()
endif()

include(GoogleTest)
