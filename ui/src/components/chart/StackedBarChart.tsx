import { BarChart } from '@mui/x-charts/BarChart';


type BasicChartProps = {
  title: string,
  data: {
    value: number[], 
    label: string | undefined,
  }[],
  labels: string[],
}

export function StackedBarChart ({
    title,
    data,
    labels,
}: BasicChartProps) {
  return (
    <>
      <div className='flex flex-col items-stretch p-5 shadow-2xl shadow-stone-500 bg-slate-100'>
        <p className='text-xl text-center'>
          {title}
        </p>
        <BarChart
          className='min-h-100'
          series={
            data.map(({value: v, label: l}) => {
              return {data: v, label: l, stack: 'total'}
            })}
          height={290}
          xAxis={[{ data: labels }]}
        />
      </div>
    </>
  );
}
