# MultiQC plugin: customize general statistics

```
# install module in same environment as multiqc
git push origin master
```

## Example

```
# Add the following entry to your multiqc config
# This example add picard metrics PF_READS_ALIGNED
# all fields used by multiqc, for example title, can be set
multiqc_cgs:
  "Picard: HsMetrics":
    ZERO_CVG_TARGETS_PCT:
      title: "Target bases with zero coverage [%]"
      description: "Target bases with zero coverage [%] from Picard"
      min: 0
      max: 100
      scale: "RdYlGn-rev"
      format: "{:.2%}"

``
