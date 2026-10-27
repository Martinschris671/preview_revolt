Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap([string](Resolve-Path "$PSScriptRoot\shot.jpg"))
$W = $bmp.Width; $H = $bmp.Height
function Rgb($c) { "{0:X2}{1:X2}{2:X2}" -f $c.R, $c.G, $c.B }
function AvgSeg($x0, $x1, $y, $vertical) {
  $r=0;$g=0;$b=0;$n=0
  for ($i=$x0; $i -le $x1; $i++) {
    if ($vertical) { $c = $bmp.GetPixel($y, $i) } else { $c = $bmp.GetPixel($i, $y) }
    $r+=$c.R; $g+=$c.G; $b+=$c.B; $n++
  }
  $col = [System.Drawing.Color]::FromArgb([int]($r/$n),[int]($g/$n),[int]($b/$n))
  Rgb $col
}
function ScanRow($y, $thr=14) {
  "ROW y=$y"
  $start=0; $prev=$bmp.GetPixel(0,$y)
  for ($x=1; $x -lt $W; $x++) {
    $c=$bmp.GetPixel($x,$y)
    $d=[Math]::Max([Math]::Abs($c.R-$prev.R),[Math]::Max([Math]::Abs($c.G-$prev.G),[Math]::Abs($c.B-$prev.B)))
    if ($d -gt $thr) {
      if ($x-$start -ge 3) { "  x {0,3}-{1,3} w{2,3} {3}" -f $start,($x-1),($x-$start),(AvgSeg $start ($x-1) $y $false) }
      $start=$x
    }
    $prev=$c
  }
  if ($W-$start -ge 3) { "  x {0,3}-{1,3} w{2,3} {3}" -f $start,($W-1),($W-$start),(AvgSeg $start ($W-1) $y $false) }
}
function ScanCol($x, $thr=14) {
  "COL x=$x"
  $start=0; $prev=$bmp.GetPixel($x,0)
  for ($y=1; $y -lt $H; $y++) {
    $c=$bmp.GetPixel($x,$y)
    $d=[Math]::Max([Math]::Abs($c.R-$prev.R),[Math]::Max([Math]::Abs($c.G-$prev.G),[Math]::Abs($c.B-$prev.B)))
    if ($d -gt $thr) {
      if ($y-$start -ge 3) { "  y {0,4}-{1,4} h{2,4} {3}" -f $start,($y-1),($y-$start),(AvgSeg $start ($y-1) $x $true) }
      $start=$y
    }
    $prev=$c
  }
  if ($H-$start -ge 3) { "  y {0,4}-{1,4} h{2,4} {3}" -f $start,($H-1),($H-$start),(AvgSeg $start ($H-1) $x $true) }
}
"W=$W H=$H"
ScanCol 6
ScanCol 369
