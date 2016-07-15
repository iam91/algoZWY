package zwy.datatype;

public abstract class Paths{
	public abstract boolean hasPathTo(int v);
	public abstract Iterable<Integer> pathTo(int v);
}