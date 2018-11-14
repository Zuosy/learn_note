cmake_minimum_required(VERSION 3.10.2)

project(hello)

message("in work dir cmake")
# message("CMAKE_BINARY_DIR " ${CMAKE_BINARY_DIR})
# message("PROJECT_BINARY_DIR " ${PROJECT_BINARY_DIR})
# message("<project_name>_BINARY_DIR " ${hello_BINARY_DIR})

# message("CMAKE_SOURCE_DIR " ${CMAKE_SOURCE_DIR})
# message("PROJECT_SOURCE_DIR " ${PROJECT_SOURCE_DIR})
# message("<project_name>_SOURCE_DIR " ${hello_SOURCE_DIR})

# message("CMAKE_CURRENT_SOURCE_DIR " ${CMAKE_CURRENT_SOURCE_DIR})
# message("CMAKE_CURRENT_BINARY_DIR " ${CMAKE_CURRENT_BINARY_DIR})

# message("CMAKE_CURRENT_LIST_FILE " ${CMAKE_CURRENT_LIST_FILE})
# message("CMAKE_CURRENT_LIST_LINE " ${CMAKE_CURRENT_LIST_LINE})

# message("CMAKE_MODULE_PATH " ${CMAKE_MODULE_PATH})

# message("EXECUTABLE_OUTPUT_PATH " ${EXECUTABLE_OUTPUT_PATH})
# message("LIBRARY_OUTPUT_PATH " ${LIBRARY_OUTPUT_PATH})

# 环境变量
# message("JAVA HOME " $ENV   {JAVA_HOME})

# add_subdirectory("src" "bin")

# User系统信息
# message("CMAKE_MAJOR_VERSION " ${CMAKE_MAJOR_VERSION})
# message("CMAKE_MINOR_VERSION " ${CMAKE_MINOR_VERSION})
# message("CMAKE_PATCH_VERSION " ${CMAKE_PATCH_VERSION})
# message("CMAKE_SYSTEM " ${CMAKE_SYSTEM})
# message("CMAKE_SYSTEM_NAME " ${CMAKE_SYSTEM_NAME})
# message("CMAKE_SYSTEM_VERSION " ${CMAKE_SYSTEM_VERSION})
# message("CMAKE_SYSTEM_PROCESSOR " ${CMAKE_SYSTEM_PROCESSOR})
# message("UNIX " ${UNIX})
# message("WIN32 " ${WIN32})

# 主要的开关
# CMAKE_ALLOW_LOOSE_LOOP_CONSTRUSTS
# 控制IF ELSE语句的书写方式
# set(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUSTS on) # 好像已经没用了
if(UNIX)
    message("This is a UNIX system.")
endif()

# BUILD_SHARED_LIBS
# set(BUILD_SHARED_LIBS ON) 使ADD_LIBRARY默认生成的库都是动态库;不设置默认生成的是静态库
# set(BUILD_SHARED_LIBS on)
# add_library(hello "hello.cpp")

# CMAKE_C_FLAGS
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c++11") # 大概这么使用吧,下面的一样

# CMAKE_CXX_FLAGS
# 彼此秒懂.jpg