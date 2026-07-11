# SovereignDCIM

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21308534.svg)](https://doi.org/10.5281/zenodo.21308534)

A theoretical architecture and functional Proof-of-Concept (PoC) for a hardware-locked, replay-resilient cyber-physical security system designed for hyper-density AI Data Centers. 

**Read the full paper on Zenodo:** [10.5281/zenodo.21308534](https://doi.org/10.5281/zenodo.21308534)

## Abstract
Conventional DCIM frameworks rely on user-space polling (creating structural latency) and software-level wiping (vulnerable to privilege escalation). SovereignDCIM strictly decouples observability, cognitive inference, and physical enforcement to establish a mathematically bounded, zero-trust infrastructure.

## Core Architecture
This repository contains the core software logic validating the theoretical bounds proposed in the paper:

1. **Kernel-Space Telemetry (`kernel/dcim_telemetry.bpf.c`)**
   - Utilizes eBPF `BPF_MAP_TYPE_RINGBUF` with memory barriers.
   - Bypasses user-space context switches to achieve strict `O(1)` latency.

2. **Thermodynamic AI Inference (`ai_engine.py`)**
   - Implements a Physics-Informed Neural Network (PINN).
   - Embeds time-lagged Navier-Stokes fluid dynamics to account for the physical thermal inertia of server chassis.

3. **Cryptographic State Machine (`auth.py`)**
   - Enforces a Deterministic Finite Automaton (DFA) Two-Man Rule over OOB interfaces.
   - Mathematically prevents network sniffing and replay attacks via strict timestamped nonces.

4. **Hardware-Locked Execution (`core/nvme_opal_purge.c`)**
   - Bypasses the OS Logical Volume Manager (LVM) entirely.
   - Dispatches raw `0x84` NVMe IOCTL opcodes for TCG OPAL 2.0 Crypto Erase in the nanosecond regime.

## Deployment Topology
Designed to run asynchronously. The I/O-bound eBPF telemetry loop (`iot_collector.py`) and the CPU-bound PINN tensor operations (`ai_engine.py`) are strictly isolated via `ProcessPoolExecutor` to overcome the Python GIL.

## Citation
If you use this architecture or PoC in your research, please cite:
```bibtex
@article{lee2026sovereigndcim,
  title={Sovereign-DCIM: A Theoretical Architecture and Proof-of-Concept for Hardware-Locked, Replay-Resilient Cyber-Physical Security in AI Data Centers},
  author={Lee, DongHyun},
  journal={Zenodo},
  year={2026},
  doi={10.5281/zenodo.21308534}
}
