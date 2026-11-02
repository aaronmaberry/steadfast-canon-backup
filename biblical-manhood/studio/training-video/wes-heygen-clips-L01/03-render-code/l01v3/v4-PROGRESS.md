# v4 progress (restart notes)
- 11:15 CT: Credits 433 -> 427 (wide test 39792921, 6 cr) -> 306 (batch 8ac896fc, 17 segs, 121 cr). Total 127. DO NOT re-render: hg_w00-w16.mp4 in /workspace/l01v4/wide, segments.json has 'clip'.
- Bubble stab test PASS (vert 35.2->17.6 px, -50%). wqc done (wqc1/wqc2.log).
- Full render: /workspace/l01v4/run_chunks.sh (skips finished chunks). c00-c02 done, c03 running.
- 11:25 CT: c00-c03 done, c04/c05 running. Next: ./finalize.sh, ./review.sh (in l01v4), qc/qc_v4.py MASTER OUT N0 N1 (2 procs), loudness, joins, ASR week scan.
- 11:24 CT: master finalized
- 11:27 CT: qc_v4 done
- 11:30 CT: review copies done
- 11:45 CT: v4 delivered + QC report. Next: silent cleanup of v3/v4 intermediates.
- cleanup done
