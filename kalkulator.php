<?php
$a       = $_GET['a'];
$b       = $_GET['b'];
$operasi = $_GET['operasi'];

echo "Nilai y : $a<br>";
echo "Nilai x : $b<br><br>";
 
if ($operasi=="jumlah"){
  $c = $a + $b; // rumus penjumlahan
  echo "Penjumlahan $a + $b = $c";
}
elseif ($operasi=="kurang"){
  $c = $a - $b; // rumus pengurangan
  echo "Pengurangan $a - $b = $c";
}
elseif ($operasi=="kali"){
  $c = $a * $b; // rumus perkalian
  echo "Perkalian $a x $b = $c";
}
elseif ($operasi=="bagi"){
  $c = $a / $b; // rumus pembagian
  echo "Pembagian $a / $b = $c";
}
// apabila operasi perhitungan belum dipilih
else{
  echo "Anda belum memilih operasi perhitungan";
}
?>