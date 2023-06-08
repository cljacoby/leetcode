CC     = gcc
# ASAN_FLAGS = -fsanitize=address -fno-omit-frame-pointer -Wno-format-security
ASAN_FLAGS = -fno-omit-frame-pointer -Wno-format-security
ASAN_LIBS = -static-libasan
CFLAGS := -Wall -Werror --std=gnu99 -g3

ARCH := $(shell uname)
ifneq ($(ARCH),Darwin)
  LDFLAGS += -lpthread
endif

SRCS :=$(wildcard *.c)
EXES :=$(SRCS:.c=)

all: $(EXES)

$(EXES):$(SRCS)
	$(CC) $< $(CFLAGS) $(ASAN_FLAGS) $(LDFLAGS) -o $@

clean:
	rm -rf $(EXES)
	rm -rf *.dSYM
