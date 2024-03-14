<script>
	export let data;
	import { pos, visible } from './store.js';

	const handleKeyDown = (e, type) => {
		let trueCondition = true;
		if (type === 'key') {
			trueCondition = e.keyCode === 17;
		}

		if (trueCondition) {
			if ($pos !== 'left-0') {
				pos.set('left-0');
				visible.set('opacity-100 z-[10]');
			} else {
				pos.set('left-[-25%]');
				visible.set('opacity-0 z-[-10]');
			}
		}
	};
</script>

<div class="bg-gradient-to-r from-slate-700 to-slate-900 h-[100vh] w-full">
	<button
		class="h-16 fill-slate-300 p-2"
		on:click={(e) => {
			handleKeyDown(e, 'click');
		}}
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 448 512"
			class="h-full px-2 py-1 border-slate-300 border-4 rounded-md"
			><path
				d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"
			/></svg
		>
	</button>
</div>
