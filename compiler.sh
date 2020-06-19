printf "%-20s %-20s %-20s %-20s %-20s\n" "Folder" "Energy" "Atoms" "E/Atom" "Runtime"
for i in */; do
  cd $i
  energy=`grep " F=" print-out | awk '{print $5}'`
  eney=`grep " F=" print-out | tail -1 | awk '{print $5}'`
  atoms=`grep -m 1 " POSCAR found :" print-out | awk '{print $7}'`
  runtime=`grep "Total CPU" RUN/OUTCAR | awk '{print$6}'`
  realnumber=`printf '%.8f' $eney`
  eperatom=`echo 'scale = 10; "$energy"/"$atoms"' | bc`
  eper=`echo "scale = 10; '$energy'/'$atoms'" | bc`

cd ../
printf "%-20s %-20s %-20s %-20s %-20s\n" "$i"  "$realnumber"  "$atoms" "$eper" "$runtime"
done
