CC     = gcc
# ASAN_FLAGS = -fsanitize=address -fno-omit-frame-pointer -Wno-format-security
ASAN_FLAGS = -fno-omit-frame-pointer -Wno-format-security
ASAN_LIBS = -static-libasan
CFLAGS := -Wall -Werror -pedantic --std=gnu99 -g3

GPP    = g++
CPP_FLAGS := -Wall -Werror -pedantic -std=c++14  

ARCH := $(shell uname)
ifneq ($(ARCH),Darwin)
  LDFLAGS += -lpthread
endif

CSRCS :=$(wildcard *.c)
CEXES :=$(CSRCS:.c=)

CPP_SRCS :=$(wildcard *.cpp)
CPP_EXES :=$(CPP_SRCS:.cpp=)

all: $(CEXES) $(CPP_EXES)

$(CEXES):$(CSRCS)
	$(CC) $< $(CFLAGS) $(ASAN_FLAGS) $(LDFLAGS) -o $@

$(CPP_EXES):$(CPP_SRCS)
	$(GPP) $< $(CPP_FLAGS) -o $@

clean:
	rm -rf $(CEXES)
	rm -rf $(CPP_EXES)
	rm -rf *.dSYM
