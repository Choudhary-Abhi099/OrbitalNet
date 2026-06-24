interface StatCardProps {
  title: string;

  value: string | number;
}

export default function StatCard({ title, value }: StatCardProps) {
  return (
    <div
      className="
               bg-slate-800
rounded-xl
p-6
border
border-cyan-900
            "
    >
      <h3
        className="
                    text-gray-400
                    text-sm
                "
      >
        {title}
      </h3>

      <p
        className="
                    text-3xl
                    font-bold
                    mt-2
                "
      >
        {value}
      </p>
    </div>
  );
}
