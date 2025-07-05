
type PageProps = {
  title: string | undefined,
  subTitle: string | undefined,
  children: React.ReactNode | undefined,
}


export function Page({
  title,
  subTitle,
  children,
}: PageProps) {
  return(
    <div id={`page-${title}`} className='flex flex-col flex-grow h-screen overflow-y-auto'>
      {title && <p className='mt-5 text-center text-4xl'>
        {title}
      </p>}
      {subTitle && <p className='m-3 text-center text-xl text-zinc-500'>
        {subTitle}
      </p>}
      {children && children}
    </div>
  )
}
