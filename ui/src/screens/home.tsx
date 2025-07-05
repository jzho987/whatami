import { Page, StackedBarChart } from "../components";

export function Home() {
  return (
    <Page title="Home"
      subTitle="view your stats and goals for the week">
      <div className='flex flex-col p-10 gap-10'>
        <StackedBarChart
          title="Hours Worked"
          data={[
            {value: [1, 2, 3, 4, 5, 6, 7], label: "working"},
            {value: [7, 6, 5, 4, 3, 2, 1], label: "resting"},
          ]}
          labels={["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
        />
      </div>
    </Page>
  )
}
