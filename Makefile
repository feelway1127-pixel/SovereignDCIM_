# SovereignDCIM Build System
CC = clang
CFLAGS = -O2 -g -Wall -Werror

# Targets
EBPF_OBJ = kernel/dcim_telemetry.bpf.o
PURGE_BIN = core/nvme_opal_purge

all: $(EBPF_OBJ) $(PURGE_BIN)

# Compile eBPF C code to object file
$(EBPF_OBJ): kernel/dcim_telemetry.bpf.c
	$(CC) $(CFLAGS) -target bpf -D__TARGET_ARCH_x86 -I/usr/include/bpf -c $< -o $@

# Compile NVMe OPAL Purge binary
$(PURGE_BIN): core/nvme_opal_purge.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f kernel/*.o core/nvme_opal_purge

.PHONY: all clean